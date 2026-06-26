---
title: "Save Table to PDF Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Table_Annotation_to_PDF_Example_VB.htm"
---

# Save Table to PDF Example (VBA)

This example shows how to save a table as a PDF file.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open a part document that contains a table annotation.
' 2. Select the table annotation.
'
' Postconditions:
' 1. Saves the selected table as c:\test\table.pdf.
' 2. Examine c:\test\table.pdf.
'-----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swTableAnnotation As SldWorks.TableAnnotation
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelectionMgr = swModel.SelectionManager
```

```
'Get the selected table and save as a PDF file
Set swTableAnnotation = swSelectionMgr.GetSelectedObject6(1, 0)
swTableAnnotation.SaveAsPDF ("c:\test\table.pdf")
```

```
End Sub
```
