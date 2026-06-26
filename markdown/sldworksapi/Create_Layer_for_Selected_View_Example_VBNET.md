---
title: "Create Layer for Selected View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Layer_for_Selected_View_Example_VBNET.htm"
---

# Create Layer for Selected View Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Private Sub ChangeComponentLayer _
     ( _
     ByVal swDraw As DrawingDoc, _
     ByVal sLayerName As String _
     )
         Dim bRet As Boolean

         ' Form a valid layer name
         sLayerName = Replace(sLayerName, "/", "_")
         sLayerName = Replace(sLayerName,  "@", "_")

         bRet = swDraw.CreateLayer2( _
                     sLayerName, _
                     "Layer for part in " & sLayerName, _
                     0, swLineStyles_e.swLineCONTINUOUS, swLineWeights_e.swLW_NORMAL, True, True)

         ' Change in all drawing views
         swDraw.ChangeComponentLayer(sLayerName, True)

     End Sub

     Sub main()

         Dim swModel As ModelDoc2
         Dim swDraw As DrawingDoc
         Dim swSelMgr As SelectionMgr
         Dim swView As View
         Dim swDrawModel As ModelDoc2
         Dim swDrawPart As PartDoc
         Dim vBody As Object
         Dim swBody As Body2
         Dim swFace As Face2
         Dim swEnt As Entity
         Dim nErrors As Long
         Dim nWarnings As Long
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swDraw = swModel
         swSelMgr = swModel.SelectionManager
         swView = swSelMgr.GetSelectedObject6(1, -1)
         swDrawModel = swApp.OpenDoc6(swView.GetReferencedModelName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", nErrors, nWarnings)
         swDrawPart = swDrawModel

         Debug.Print("File           = " & swModel.GetPathName)
         Debug.Print("  View         = " & swView.Name)
         Debug.Print("    View Model = " & swView.GetReferencedModelName)

         vBody = swDrawPart.GetBodies2(swBodyType_e.swSolidBody, True)

         swBody = vBody(0)
         swFace = swBody.GetFirstFace
         swEnt = swFace

         bRet = swView.SelectEntity(swEnt,  False)

         ChangeComponentLayer(swDraw, swView.Name)

     End Sub

     Public swApp As SldWorks

 End  Class
```
