from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse

from app.processor import ImageProcessor




app = FastAPI(
    title="Product Card Processor API",
    version="0.19.0",
    description="API for batch processing marketplace product images.",
)


class EchoRequest(BaseModel):
    message: str
    workers: int = 1


class ProcessRequest(BaseModel):
    input_folder: str = "data/input"
    output_folder: str = "data/output_api"

    canvas_width: int = 1080
    canvas_height: int = 1440
    allow_upscale: bool = True

    template_path: str | None = None
    offset_x: int = 0
    offset_y: int = 0
    product_scale: float = 0.8

    remove_bg: bool = False
    bg_backend: str = "rembg"
    bg_model: str = "u2net"

    workers: int = 1

    save_report: bool = False
    report_path: str | None = None


@app.get("/")
def root():
    return {
        "service": "product-card-processor",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "product-card-processor",
        "version": "0.19.0",
    }


@app.post("/echo")
def echo(request: EchoRequest):
    return {
        "message": request.message,
        "workers": request.workers,
    }


@app.post("/process")
def process_images(request: ProcessRequest):
    try:
        processor = ImageProcessor(
            input_folder=Path(request.input_folder),
            output_folder=Path(request.output_folder),
            canvas_width=request.canvas_width,
            canvas_height=request.canvas_height,
            allow_upscale=request.allow_upscale,
            template_path=Path(request.template_path) if request.template_path else None,
            offset_x=request.offset_x,
            offset_y=request.offset_y,
            product_scale=request.product_scale,
            remove_bg=request.remove_bg,
            bg_backend=request.bg_backend,
            bg_model=request.bg_model,
            workers=request.workers,
        )

        processor.process_all_images()

        report = processor.get_report()

        if request.save_report:
            report_path = Path(request.report_path) if request.report_path else Path(request.output_folder) / "report.json"
            processor.save_report(report_path)
            report["report_path"] = str(report_path)

        return {
            "status": "completed",
            "report": report,
        }

    except (FileNotFoundError, NotADirectoryError, ValueError) as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {error}",
        )

@app.get("/ui")
def web_ui():
    return FileResponse("web/index.html")