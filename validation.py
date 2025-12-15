import datetime as dt
from app import compute_solunar_index   # import from your app.py

# PDF star ratings for December 2025 (Contoocook, NH)
PDF_STARS_BY_DAY = {
    1: 1, 2: 2, 3: 3, 4: 4, 5: 4,
    6: 3, 7: 1, 8: 1, 9: 1, 10: 1,
    11: 1, 12: 1, 13: 1, 14: 1, 15: 1,
    16: 1, 17: 3, 18: 3, 19: 4, 20: 4,
    21: 3, 22: 2, 23: 1, 24: 1, 25: 1,
    26: 1, 27: 1, 28: 1, 29: 1, 30: 1,
    31: 1
}

# Map DeerMove’s 1–6 rating to SolunarForecast’s 1–4 star buckets
def rating_to_stars(rating):
    if rating <= 2:
        return 1      # Average
    elif rating == 3:
        return 2      # Good
    elif rating == 4 or rating == 5:
        return 3      # Better
    else:
        return 4      # Best

def validate_december_2025(lat=43.2032394, lon=-71.6730576):
    print("Date        P%    Index  Rate  DeerST  PDFST   Match")
    print("-----------------------------------------------------")

    matches = 0
    total = 31

    for day in range(1, 32):
        date = dt.date(2025, 12, day)

        index, rating, phase = compute_solunar_index(date, lat, lon)

        deer_stars = rating_to_stars(rating)
        pdf_stars = PDF_STARS_BY_DAY[day]

        match = (deer_stars == pdf_stars)
        if match:
            matches += 1

        print(
            f"{date}  {phase:5.1f}  {index:5.2f}    {rating}      "
            f"{deer_stars}       {pdf_stars}     {match}"
        )

    print(f"\nMATCHES: {matches}/{total} days")

if __name__ == "__main__":
    validate_december_2025()
