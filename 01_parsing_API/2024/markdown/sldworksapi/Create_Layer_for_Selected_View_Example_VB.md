---
title: "Create Layer for Selected View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Layer_for_Selected_View_Example_VB.htm"
---

# Create Layer for Selected View Example (VBA)

This example shows how to create a layer for the part in the selected drawing view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing of a part.
 ' 2. Select a drawing view in the FeatureManager design tree.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a layer for the part in the selected drawing view.
 ' 2. Click the Layer Properties tool on the Line Format toolbar to verify
 '    that the newly created layer is selected in the Layers dialog box.
 ' 3. Examine the Immediate window.
 '----------------------------------------------------------------------------
 Option Explicit

 Private Sub ChangeComponentLayer _
 ( _
     swApp As SldWorks.SldWorks, _
     swDraw As SldWorks.DrawingDoc, _
     sLayerName As String _
 )
     Dim bRet                    As Boolean
    ' Form a valid layer name
     sLayerName = Replace(sLayerName, "/", "_")
     sLayerName = Replace(sLayerName, "@", "_")
    bRet = swDraw.CreateLayer2( _
                 sLayerName, _
                 "Layer for part in " & sLayerName, _
                 0, swLineCONTINUOUS, swLW_NORMAL, True, True)
    ' Change in all drawing views
     swDraw.ChangeComponentLayer sLayerName, True
End Sub
Sub main()
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
     Dim nErrors As Long
     Dim nWarnings As Long
     Dim bRet As Boolean

    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swDraw = swModel
     Set swSelMgr = swModel.SelectionManager
     Set swView = swSelMgr.GetSelectedObject6(1, -1)
     Set swDrawModel = swApp.OpenDoc6(swView.GetReferencedModelName, swDocPART, swOpenDocOptions_Silent, "", nErrors, nWarnings)
     Set swDrawPart = swDrawModel
    Debug.Print "File           = " & swModel.GetPathName
     Debug.Print "  View         = " & swView.Name
     Debug.Print "    View Model = " & swView.GetReferencedModelName

    vBody = swDrawPart.GetBodies2(swSolidBody, True)
    Set swBody = vBody(0)
     Set swFace = swBody.GetFirstFace
     Set swEnt = swFace
    bRet = swView.SelectEntity(swEnt, False)

    ChangeComponentLayer swApp, swDraw, swView.Name
End Sub
```
