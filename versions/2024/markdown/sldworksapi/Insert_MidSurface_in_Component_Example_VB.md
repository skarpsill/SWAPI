---
title: "Insert MidSurface in Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_MidSurface_in_Component_Example_VB.htm"
---

# Insert MidSurface in Component Example (VBA)

This example shows how to insert a midsurface feature in a component.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open an assembly that contains at least one component
'    that contains a solid body.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a midsurface feature in the component.
' 2. Gets the number of faces in the midsurface feature.
' 3. Examine the Immediate window.
' 4. Expand the component in the FeatureManager design tree
'    in which the midsurface feature was inserted to
'    verify step 1.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swComp As SldWorks.Component2
Dim swAssem As SldWorks.AssemblyDoc
Dim featMgr As SldWorks.FeatureManager
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set featMgr = swModel.FeatureManager
    Set swAssem = swModel
```

```
    Dim vComponents As Variant
    vComponents = swAssem.GetComponents(True)
    Set swComp = vComponents(0)
    Dim vBodies As Variant
    vBodies = swComp.GetBodies2(swBodyType_e.swSolidBody)
    If Not IsEmpty(vBodies) Then
        Dim pBody As Body2
        Set pBody = vBodies(0)
        Dim midSurf As MidSurface3
        Set swModel = swComp.GetModelDoc2
        Debug.Print "Component in which to insert midsurface feature: " & swModel.GetPathName
        Set midSurf = featMgr.InsertMidSurface(pBody, swModel, 0.5, True)
        Debug.Print "Face count: " & midSurf.GetFaceCount
    Else
        Debug.Print "Open a different assembly in which the specified body is a solid body."
    End If
```

```
End Sub
```
