---
title: "Determine if Layer is Visible Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Determine_if_Layer_is_Visible_Example_VB.htm"
---

# Determine if Layer is Visible Example (VBA)

This example shows how to determine if a layer in a drawing is visible.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing of a part.
' 2. Select a drawing view in the FeatureManager design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a layer of the part in the selected drawing view.
' 2. Gets whether the layer is visible.
' 3. Examine the Immediate window and drawing.
'----------------------------------------------------------------------------
Option Explicit
```

```
Private Sub ChangeComponentLayer _
( _
    swApp As SldWorks.SldWorks, _
    swDraw As SldWorks.DrawingDoc, _
    sLayerName As String _
)
    Dim bRet As Boolean
```

```
    sLayerName = "Layer1"
    bRet = swDraw.CreateLayer2( _
                sLayerName, _
                "Layer for part in " & sLayerName, _
                0, swLineCONTINUOUS, swLW_NORMAL, True, True)
```

```
    ' Change in all views
    swDraw.ChangeComponentLayer sLayerName, True
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swView As SldWorks.View
    Dim swDrawModel As SldWorks.ModelDoc2
    Dim swDrawPart As SldWorks.PartDoc
    Dim vBody As Variant
    Dim swBody As SldWorks.Body2
    Dim swFace As SldWorks.Face2
    Dim swEnt As SldWorks.Entity
    Dim swLayerMgr As SldWorks.LayerMgr
    Dim swLayer As SldWorks.Layer
    Dim nErrors As Long
    Dim nWarnings As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
    Set swDrawModel = swApp.OpenDoc6(swView.GetReferencedModelName, swDocPART, swOpenDocOptions_Silent, "", nErrors, nWarnings)
    Set swDrawPart = swDrawModel
```

```
    vBody = swDrawPart.GetBodies2(swSolidBody, True)
```

```
    Set swBody = vBody(0)
    Set swFace = swBody.GetFirstFace
    Set swEnt = swFace
```

```
    bRet = swView.SelectEntity(swEnt, False)
```

```
    ChangeComponentLayer swApp, swDraw, swView.Name
```

```
    Set swLayerMgr = swModel.GetLayerManager
    Set swLayer = swLayerMgr.GetLayer("Layer1")
    Debug.Print "Layer visible?" & swLayer.Visible
```

```
End Sub
```
