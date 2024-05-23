import pickle

try:
    with open(r"C:\Users\ABDUL REHMAN\Desktop\StayFIT App\Stayfit\Stayfit\Stay_Fit_with_Abdul\deadlift.pkl", 'rb') as f: 
        model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except pickle.PickleError:
    print("Error: Unable to load the pickle file.")
except Exception as e:
    print("An unexpected error occurred:", e)
