---
title: "Get Surface Type Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Surface_Type_Example_VB.htm"
---

# Get Surface Type Example (VBA)

This example shows how to get the type of surface.

```
'----------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select a face on the part.
'
' Postconditions: Examine the Immediate window.
'-----------------------------------------
Option Explicit
```

```
Public Enum swSurfaceTypes_e
    PLANE_TYPE = 4001
    CYLINDER_TYPE = 4002
    CONE_TYPE = 4003
    SPHERE_TYPE = 4004
    TORUS_TYPE = 4005
    BSURF_TYPE = 4006
    BLEND_TYPE = 4007
    OFFSET_TYPE = 4008
    EXTRU_TYPE = 4009
    SREV_TYPE = 4010
End Enum
```

```
Sub main()
```

```
    Dim swSurfaceTypes(10)      As String
    swSurfaceTypes(1) = "PLANE"
    swSurfaceTypes(2) = "CYLINDER"
    swSurfaceTypes(3) = "CONE"
    swSurfaceTypes(4) = "SPHERE"
    swSurfaceTypes(5) = "TORUS"
    swSurfaceTypes(6) = "BSURF"
    swSurfaceTypes(7) = "BLEND"
    swSurfaceTypes(8) = "OFFSET"
    swSurfaceTypes(9) = "EXTRU"
    swSurfaceTypes(10) = "SREV"
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim swSurf As SldWorks.Surface
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject5(1)
    Set swSurf = swFace.GetSurface
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Identity = " & swSurfaceTypes(swSurf.Identity - 4000)

End Sub
```
