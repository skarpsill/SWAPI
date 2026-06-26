---
title: "Get Parameters of Reference Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parameters_of_Reference_Plane_Example_VB.htm"
---

# Get Parameters of Reference Plane Example (VBA)

This example shows how to get the parameters of a reference plane.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a model document containing a reference
'    plane.
' 2. Select the reference plane.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the parameters of the selected reference
'    plane.
' 2. Examine the Immediate window.
'
' NOTES:
' * Origin is translation vector from
'   plane origin -> model origin
'   wrt plane coordinate system.
' * Xvector is wrt model coordinate system.
' * Normal is wrt model coordinate system.
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
    Dim swFeat As SldWorks.Feature
    Dim swRefPlane As SldWorks.RefPlane
    Dim vPlaneParam As Variant
    Dim nDist As Double
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swRefPlane = swFeat.GetSpecificFeature2
```

```
    vPlaneParam = swRefPlane.GetRefPlaneParams
    Debug.Print "Plane = " + swFeat.Name
```

```
    Debug.Print "  Model Origin (wrt Plane) = (" + Str(vPlaneParam(0) * 1000#) + "," + Str(vPlaneParam(1) * 1000#) + "," + Str(vPlaneParam(2) * 1000#) + ") mm"
    Debug.Print "  Xvector      (wrt Model) = (" + Str(vPlaneParam(3)) + "," + Str(vPlaneParam(4)) + "," + Str(vPlaneParam(5)) + ")"
    Debug.Print "  Normal       (wrt Model) = (" + Str(vPlaneParam(6)) + "," + Str(vPlaneParam(7)) + "," + Str(vPlaneParam(8)) + ")"
    nDist = Sqr(vPlaneParam(0) ^ 2 + vPlaneParam(1) ^ 2 + vPlaneParam(2) ^ 2)
    Debug.Print "  Plane Origin (wrt Model) = (" + Str(nDist * vPlaneParam(6) * 1000#) + "," + Str(nDist * vPlaneParam(7) * 1000#) + "," + Str(nDist * vPlaneParam(8) * 1000#) + ") mm"
```

```
End Sub
```
