def predict_label(value):
    """A tiny example function for CI testing."""
    return "positive, definitely" if value >= 0.5 else "negative"

if __name__ == "__main__":
    print("Model prediction for 0.8:", predict_label(0.8))
