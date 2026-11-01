# Suggested evaluation plan

Use a small manually checked test set with at least 30 sentences:
- 10 simple sentences
- 10 compound sentences
- 10 complex sentences

For each sentence, manually record the expected POS tags and head/dependency labels. Compare the application's predictions with the manual reference.

Report:
- POS accuracy = correctly predicted POS tags / total evaluated tokens
- Head accuracy = correctly predicted dependency heads / total evaluated tokens
- Dependency-label accuracy = correctly predicted dependency labels / total evaluated tokens

Be clear that the manually annotated reference set is a small course-project evaluation and not a benchmark dataset.
