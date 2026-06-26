---
title: "Get DimXpert Features and Annotations in a Model Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Features_and_Annotations_in_a_Model_Example_CSharp.htm"
---

# Get DimXpert Features and Annotations in a Model Example (C#)

This application shows you how to get all of the DimXpert
feature and annotation objects in a model.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

This application is more advanced than other examples,
because it involves multiple class modules.

```vb
 //--------------------------------------------------------------------------
// Preconditions:
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Create a new C# macro using SOLIDWORKS VSTA.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2. Name the project DimXpert_text_v2_cs.
// kadov_tag{{<spaces>}}3. Save the project.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}4. Copy and paste the Main module into the code window. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
// kadov_tag{{<spaces>}}5. Right-click on the project in Project Explorer and click Add > Class.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}6. Select the Class template and type DimXpertFeatureData.cs
//    in the Name field.
// kadov_tag{{<spaces>}}7. Click Add.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}8. Copy and paste the DimXpertFeatureData class module into the code window. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}9. Right-click on the project in Project Explorer and click Add > Class.
// kadov_tag{{<spaces>}}10. Select the Class template and type DimXpertAnnotationData.cs
//     in the Name field.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}11. Click Add.
// kadov_tag{{<spaces>}}12. Copy and paste the DimXpertAnnotationData class module
//     into the code window. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
// kadov_tag{{<spaces>}}13. Ensure that the latest SolidWorks.Interop.swdimxpert.dll interop assembly
//     is loaded (right-click on the project in Project Explorer,
//     click Add Reference, choose the DimXpert assembly on the .NET tab).
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}14. Ensure that the Microsoft Scripting Runtime library is loaded
// kadov_tag{{<spaces>}}    (right-click on the project in Project Explorer, click Add Reference,
//      choose the library on the COM tab).
// kadov_tag{{<spaces>}}15. Open a part that contains DimXpert features and/or annotations.
// kadov_tag{{<spaces>}}    (You may want to go through the online DimXpert Tutorial
//      to learn how to create DimXpert features and annotations.
// kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}From the ? help menu, click SOLIDWORKS Tutorials > All SOLIDWORKS
//      Tutorials (Set 1) > DimXpert Tutorials)
// kadov_tag{{<spaces>}}16. Open an Immediate Window in the IDE.
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}17. Run this macro (F5).
//
// Postconditions:
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. The output of this macro is logged in c:\temp\dimXpertInfo.txt.
// kadov_tag{{<spaces>}}2. kadov_tag{{</spaces>}}Inspect the Immediate Window.
//--------------------------------------------------
```
