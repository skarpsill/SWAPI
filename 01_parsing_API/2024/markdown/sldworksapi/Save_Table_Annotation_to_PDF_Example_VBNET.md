---
title: "Save Table to PDF Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Table_Annotation_to_PDF_Example_VBNET.htm"
---

# Save Table to PDF Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSelectionMgr As SelectionMgr
        Dim swTableAnnotation As TableAnnotation

        swModel = swApp.ActiveDoc
        swSelectionMgr = swModel.SelectionManager

        'Get the selected table and save as a PDF file
        swTableAnnotation = swSelectionMgr.GetSelectedObject6(1, 0)
        swTableAnnotation.SaveAsPDF("c:\test\table.pdf")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
