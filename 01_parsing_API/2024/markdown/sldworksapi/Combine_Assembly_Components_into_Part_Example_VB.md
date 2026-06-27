---
title: "Combine Assembly Components into Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Combine_Assembly_Components_into_Part_Example_VB.htm"
---

# Combine Assembly Components into Part Example (VBA)

This example shows how to combine two assembly components into a part.

```
'------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\landing_gear.sldasm.
' 2. In the FeatureManager design tree:
'    a. Click oleostrut<1>.
'    b. Ctrl+click oleopiston<1>.
'    NOTE: Both components are single-body components that
'    only contain solid bodies.
' 3. Verify that the specified part document template exists.
'
' Postconditions:
' 1. Creates a new part, which is a Boolean addition of both
'    selected components.
' 2. Click Zoom to Fit.
'
' NOTES:
' * This example:
'   * does not replace saving an assembly as a part.
'   * only illustrates the use of several geometric and
'     topological methods and properties.
' * Because the assembly is used elsewhere, do not save
'   changes.
'------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp1 As SldWorks.Component2
    Dim swComp2 As SldWorks.Component2
    Dim swXform1 As SldWorks.MathTransform
    Dim swXform2 As SldWorks.MathTransform
    Dim swBody1 As SldWorks.Body2
    Dim swBody1Copy As SldWorks.Body2
    Dim swBody2 As SldWorks.Body2
    Dim swBody2Copy As SldWorks.Body2
    Dim vBodyResArr As Variant
    Dim vBodyRes As Variant
    Dim swBodyRes As SldWorks.Body2
    Dim swPartRes  As SldWorks.PartDoc
    Dim swFeatRes As SldWorks.Feature
    Dim nRetval As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swComp1 = swSelMgr.GetSelectedObjectsComponent2(1)
    Set swComp2 = swSelMgr.GetSelectedObjectsComponent2(2)
    Set swXform1 = swComp1.Transform2
    Set swXform2 = swComp2.Transform2
```

```
    Set swBody1 = swComp1.GetBody
    Set swBody2 = swComp2.GetBody
    Set swBody1Copy = swBody1.Copy
    Set swBody2Copy = swBody2.Copy
```

```
    bRet = swBody1Copy.ApplyTransform(swXform1)
    bRet = swBody2Copy.ApplyTransform(swXform2)
```

```
    vBodyResArr = swBody1Copy.Operations2(SWBODYADD, swBody2Copy, nRetval)
    Debug.Assert Not IsEmpty(vBodyResArr)
```

```
    Set swPartRes = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2014\templates\Part.prtdot", 0, 0, 0)
    For Each vBodyRes In vBodyResArr
        Set swBodyRes = vBodyRes
        Set swFeatRes = swPartRes.CreateFeatureFromBody3(swBodyRes, False, swCreateFeatureBodyCheck + swCreateFeatureBodySimplify): Debug.Assert Not swFeatRes Is Nothing
    Next
```

```
End Sub
```
