from fastapi import FastAPI, Query, HTTPException
from models import MenuItem, MenuResponse
from data import menuItems


app  = FastAPI(
    title="Restaurant Menu API",
    description="API for managing restaurant menu items",
    docs_url="/docs",

);


@app.get("/")
def root():
    return {"message":"Welcome to new app"}

@app.get("/menu", response_model=MenuResponse)
def get_menu(
    category: str | None = Query(None, description="Filter by category", min_length=3, max_length=20, example="drinks"),
):
    if category:
        filtered = [item for item in menuItems if item["category"].lower() == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail=f"No menu items found for category '{category}'")
        return MenuResponse(status="success", count=len(filtered), menu_items=filtered)

    return MenuResponse(status="success", count=len(menuItems), menu_items=menuItems)

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_menu_item(item_id: int):
    for item in menuItems:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Menu item with id {item_id} not found")