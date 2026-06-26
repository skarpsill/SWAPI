---
title: "Get Normal of Planar Surface Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Normal_of_Planar_Surface_Example_VB.htm"
---

# Get Normal of Planar Surface Example (VBA)

This example shows how to the normal parameters of a planar surface.

```
'----------------------------------------------
' Preconditions:
' 1. Open a part, assembly, or drawing.
' 2. Select a face on a planar surface.
' 3. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: The normal of a surface (ISurface::PlaneParams)
' cannot be in the same direction as the normal
' of the face (IFace2::Normal).
'---------------------------------------------
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
    Dim vPlaneParam As Variant
    Dim vFaceNorm As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject5(1)
    Set swSurf = swFace.GetSurface: Debug.Assert swSurf.IsPlane
    vPlaneParam = swSurf.PlaneParams
    vFaceNorm = swFace.Normal
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Surface"
    Debug.Print "    normal               = (" & vPlaneParam(0) & ", " & vPlaneParam(1) & ", " & vPlaneParam(2) & ")"
    Debug.Print "    root                 = (" & vPlaneParam(3) * 1000# & ", " & vPlaneParam(4) * 1000# & ", " & vPlaneParam(5) * 1000# & ") mm"
    Debug.Print "  Face"
    Debug.Print "    normal               = (" & vFaceNorm(0) & ", " & vFaceNorm(1) & ", " & vFaceNorm(2) & ")"
    Debug.Print "    true if face normal and surface normal in opposite direction, false if in same direction = " & swFace.FaceInSurfaceSense
```

```
End Sub
```
