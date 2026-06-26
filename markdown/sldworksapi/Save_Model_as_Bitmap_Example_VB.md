---
title: "Save Model as Bitmap Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_Model_as_Bitmap_Example_VB.htm"
---

# Save Model as Bitmap Example (VBA)

This example shows how to save the current view of a model as a bitmap.

```
'-----------------------------------------------------------------------------------
' Preconditions:
' 1. Open:
'    C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt
' 2. Run macro.
'
' Postconditions: Current view of the model is saved as C:\cstick.bmp.
'------------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim returnVal As Boolean
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    fileName = "c:\cstick.bmp"
```

```
    ' Save as bitmap and use current window size
    returnVal = swModel.SaveBMP(fileName, 0, 0)
```

```
End Sub
```
