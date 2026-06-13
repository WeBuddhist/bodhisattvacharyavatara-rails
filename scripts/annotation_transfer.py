from fast_antx.core import transfer

source = "सुगतान् ससुतान् सधर्मकायान् प्रणिपत्यादरतोऽखिलांश्च वन्द्यान्। ⤵सुगतात्मजसंवरावतारंकथयिष्यामि यथागमं समासात्॥ i am samdup"
target = "सुगतान् ab ससुतान् सधर्मकायान् c प्रणिपत्यादरतोऽखिलांश्च वन्द्यान्। सुगतात्मजसंवरावतारं कथयिष्यामि यथागमं समासात्॥"
patterns = [
    ["segment", r"(⤵)"]
]

# output: "txt" | "yaml" | "diff"
annotated = transfer(source, patterns, target, "txt")
print(annotated)