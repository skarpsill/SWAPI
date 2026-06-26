---
title: "Get Parameters of Conical Surface Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parameters_of_Conical_Surface_Example_VB.htm"
---

# Get Parameters of Conical Surface Example (VBA)

This example shows how to get the parameters of a conical surface.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document with a conical surface.
 ' 2. Select the conical surface.
 ' 3. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFace                  As SldWorks.Face2
     Dim swSurf                  As SldWorks.Surface
     Dim vCone                   As Variant
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFace = swSelMgr.GetSelectedObject6(1, -1)
     Set swSurf = swFace.GetSurface
    If swSurf.IsCone Then
         vCone = swSurf.ConeParams2
         Debug.Print "Origin               = (" & vCone(0) * 1000# & "mm, " & vCone(1) * 1000# & "mm, " & vCone(2) * 1000# & "mm)"
         Debug.Print "Axis                 = (" & vCone(3) & ", " & vCone(4) & ", " & vCone(5) & ")"
         Debug.Print "Radius               = " & vCone(6) * 1000# & " mm"
         ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
         Debug.Print "Half angle           = " & vCone(7) * 57.3 & " degrees"
         Debug.Print "Reference direction  = (" & vCone(8) * 1000# & "mm, " & vCone(9) * 1000# & "mm, " & vCone(10) * 1000# & "mm)"
     End If
End Sub
```
