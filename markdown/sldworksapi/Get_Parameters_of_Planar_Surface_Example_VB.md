---
title: "Get Parameters of Planar Surface Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parameters_of_Planar_Surface_Example_VB.htm"
---

# Get Parameters of Planar Surface Example (VBA)

This example shows how to get the parameters of a planar surface.

```
'----------------------------------------------
' Preconditions:
' 1. Open a part that contains a planar surface.
' 2. Select the planar surface.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim swSurf As SldWorks.Surface
    Dim vPlane As Variant

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject5(1)
    Set swSurf = swFace.GetSurface
    If swSurf.IsPlane Then
        vPlane = swSurf.PlaneParams
        Debug.Print "File = " & swModel.GetPathName
        Debug.Print "  Normal         = (" & vPlane(0) & ", " & vPlane(1) & ", " & vPlane(2) & ")"
        Debug.Print "  Root           = (" & vPlane(3) * 1000# & ", " & vPlane(4) * 1000# & ", " & vPlane(5) * 1000# & ") mm"
    End If
```

```
End Sub
```
