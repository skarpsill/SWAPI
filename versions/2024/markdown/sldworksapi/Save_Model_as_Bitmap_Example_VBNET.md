---
title: "Save Model as Bitmap Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Model_as_Bitmap_Example_VBNET.htm"
---

# Save Model as Bitmap Example (VB.NET)

```
This example shows how to save the current view of a model as a bitmap.
```

```
'-----------------------------------------------------------------------------------
' Preconditions:
' 1. Open:
'    C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt
' 2. Run macro.
'
' Postconditions: Current view of the model is saved as C:\cstick.bmp.
'------------------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim returnVal As Boolean
        Dim fileName As String

        swModel = swApp.ActiveDoc
        fileName = "c:\cstick.bmp"

        ' Save as bitmap and use current window size
        returnVal = swModel.SaveBMP(fileName, 0, 0)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
