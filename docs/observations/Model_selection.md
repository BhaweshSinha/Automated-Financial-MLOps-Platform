# Model Selection Analysis

## Objective

The objective of this phase was to evaluate multiple machine learning models and select the most suitable model for predicting stock price movement. The problem is formulated as a **binary classification task**, where:

* **1 → Stock price expected to go up**
* **0 → Stock price expected to go down**

The focus was not only on accuracy but also on selecting a model that generalizes well and performs reliably on unseen financial data.

---

## Models Evaluated

The following machine learning models were trained and compared:

* Logistic Regression
* Random Forest Classifier
* Gradient Boosting Classifier
* XGBoost Classifier

Each model was trained using the same dataset and evaluated using consistent metrics to ensure fair comparison.

---

## Performance Comparison

| Model               | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------------- | -------- | --------- | ------ | -------- | ------- |
| Logistic Regression | 0.7985   | 0.5540    | 0.5696 | 0.5617   | 0.8152  |
| Random Forest       | 0.8240   | 0.7177    | 0.3680 | 0.4866   | 0.8332  |
| Gradient Boosting   | 0.8400   | 0.7400    | 0.4535 | 0.5624   | 0.8465  |
| XGBoost             | 0.8373   | 0.7333    | 0.4440 | 0.5531   | 0.8445  |

---

## Key Observations

* **Gradient Boosting achieved the highest ROC-AUC (0.8465)**, indicating superior ability to distinguish between classes.
* **Random Forest showed high precision but very low recall**, meaning it failed to identify many positive cases.
* **Logistic Regression provided stable but lower overall performance**, indicating limitations in capturing complex relationships.
* **XGBoost performed competitively**, but slightly underperformed compared to Gradient Boosting in ROC-AUC.

---

## Model Selection Criteria

The final model selection was based on the following criteria:

* **ROC-AUC Score** (Primary Metric)
  Measures the model's ability to distinguish between classes across thresholds.

* **Balance Between Precision and Recall**
  Ensures the model is not biased toward one class.

* **Generalization Capability**
  Ability to perform well on unseen data.

* **Suitability for Financial Time-Series Data**
  Capability to handle non-linear relationships and noise in market data.

---

## Final Model Selected

**Gradient Boosting Classifier**

---

## Justification for Selection

Gradient Boosting was selected as the final model because:

* It achieved the **highest ROC-AUC score**, indicating strong classification capability.
* It maintained a **good balance between precision and recall**, unlike Random Forest.
* It is well-suited for **tabular financial data**, capturing complex, non-linear patterns.
* It demonstrated **consistent performance across multiple evaluation metrics**.
* It is computationally efficient and easier to integrate into production pipelines compared to more complex alternatives.

---

## Business Perspective

From a financial standpoint:

* A reliable classification model helps in **predicting market direction**, which is crucial for trading strategies.
* A higher ROC-AUC ensures **better decision-making under uncertainty**.
* Balanced precision and recall reduce the risk of **false trading signals**, improving robustness.

---

## Conclusion

The model selection phase ensured that the chosen model is not only accurate but also robust, reliable, and suitable for real-world deployment.

The **Gradient Boosting Classifier** was selected as the final model due to its superior performance and ability to generalize effectively on financial data.

---

## Next Steps

Following model selection:

* The model was serialized and saved for reuse
* Integrated into a prediction pipeline
* Exposed via a FastAPI-based inference service

This completes the transition from experimentation to a **production-ready machine learning system**.
