# Traffic
**c. Challenges and Observations**
- Overfitting: The model initially performed well on training data but struggled with new images. To fix this, I used dropout layers and trained with more varied images.
- Incorrect Predictions: The model frequently misclassified traffic signs, especially those with similar shapes/colors (e.g., speed limit vs. roundabout signs).

**b. Testing the Model with Tkinter**
I built the Tkinter GUI to allow users to upload images for real-time predictions. However, during testing, the model:
- Occasionally produced low-confidence scores, leading to uncertain predictions.
To address these issues, I retrained the model multiple times with different data augmentations (rotation, brightness changes) to improve generalization.

**c.  Notices**
- Upon adding various categories to the category label, the prediction where more or less the same for most of the choosen image signs except for the no entry image which prediction was right

**d. Final Results**
After multiple adjustments, the model correctly identified the no entry traffic sign with an unchanged confidence scores.
