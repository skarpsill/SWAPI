---
title: "Get Parameters of Toroidal Surface Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parameters_of_Toroidal_Surface_Example_VB.htm"
---

# Get Parameters of Toroidal Surface Example (VBA)

This example shows how to get the parameters of a toroidal surface.

```
'----------------------------------------------
' Preconditions:
' 1. Open a part that has a toroidal surface.
' 2. Select the toroidal surface.
'
' Postconditions: Examine the Immediate window.
'-----------------------------------------------
```

```
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
    Dim vTorus As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject5(1)
    Set swSurf = swFace.GetSurface
    If swSurf.IsTorus Then
        vTorus = swSurf.TorusParams
        Debug.Print "File = " & swModel.GetPathName
        Debug.Print "  center         = (" & vTorus(0) * 1000# & ", " & vTorus(1) * 1000# & ", " & vTorus(2) * 1000# & ") mm"
        Debug.Print "  axis           = (" & vTorus(3) & ", " & vTorus(4) & ", " & vTorus(5) & ")"
        Debug.Print "  major radius   = " & vTorus(6) * 1000# & " mm"
        Debug.Print "  minor radius   = " & vTorus(7) * 1000# & " mm"
    End If
```

```
End Sub
```
