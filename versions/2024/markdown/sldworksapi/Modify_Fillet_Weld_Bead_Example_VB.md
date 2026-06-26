---
title: "Modify Fillet Weld Bead Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Fillet_Weld_Bead_Example_VB.htm"
---

# Modify Fillet Weld Bead Example (VBA)

This example shows how to modify a fillet weld bead.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Inspect the Immediate window to see the properties of Fillet Bead1.
 ' 2. Modifies some properties of Fillet Bead1.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swWeldBead As SldWorks.WeldmentBeadFeatureData
 Dim swFeat As SldWorks.Feature
 Dim swSelData As SldWorks.SelectData
 Dim v1 As SldWorks.Vertex
 Dim v2 As SldWorks.Vertex
 Dim set1 As Variant
 Dim faceVar As Variant
 Dim ve As Variant
 Dim fVar1 As Variant
 Dim fVar2 As Variant
 Dim f1(0) As Object
 Dim f2(1) As Object
 Dim e(0) As Object
 Dim bdlen As Double
 Dim bdPitch As Double
 Dim bdsz As Double
 Dim bdTy As Long
 Dim i As Long
 Dim boolstatus As Boolean

Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData

    'Select Fillet Bead1 feature
     boolstatus = swModelDocExt.SelectByID2("Fillet Bead1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swWeldBead = swFeat.GetDefinition

    'Roll back to the feature just before Fillet Bead1
     boolstatus = swWeldBead.AccessSelections(swModel, Nothing)

    'Get Fillet Bead1 properties
     Debug.Print "Fillet Bead1 properties:"
     bdlen = swWeldBead.BeadLength(swWeldBeadArrowSide)
     Debug.Print "  Weld bead length: " & bdlen

    bdPitch = swWeldBead.BeadPitch(swWeldBeadArrowSide)
     Debug.Print "  Weld bead pitch: " & bdPitch

    bdsz = swWeldBead.BeadSize(swWeldBeadArrowSide)
     Debug.Print "  Weld bead size: " & bdsz

    bdTy = swWeldBead.BeadType(swWeldBeadArrowSide)
     Debug.Print "  Weld bead type as defined in swWeldBeadType_e: " & bdTy

    Debug.Print "  Propagate the weld bead along the tangent? " & swWeldBead.TangentPropagation
     Debug.Print "  Apply weld bead to both sides of intersecting faces? " & swWeldBead.UseOtherSide

    'Get Fillet Bead1 faces
     swWeldBead.GetFaces swWeldBeadArrowSide, set1, faceVar

    For i = LBound(faceVar) To UBound(faceVar)
         faceVar(i).Select4 True, swSelData
     Next i

    For i = LBound(set1) To UBound(set1)
         set1(i).Select4 True, swSelData
     Next i

    'Get Fillet Bead1 virtual edges
     ve = swWeldBead.GetVirtualEdges(False, swWeldBeadArrowSide)

    For i = LBound(ve) To UBound(ve)
         boolstatus = ve(i).Select4(True, swSelData)
         Set v1 = ve(i).GetStartVertex
         Set v2 = ve(i).GetEndVertex
     Next i

    swModel.ClearSelection2 True

    'Set new properties of Fillet Bead1
     swWeldBead.BeadLength(swWeldBeadArrowSide) = bdlen * 0.5
     swWeldBead.BeadPitch(swWeldBeadArrowSide) = bdPitch * 0.5
     swWeldBead.BeadSize(swWeldBeadArrowSide) = bdsz * 0.5
     swWeldBead.BeadType(swWeldBeadArrowSide) = bdTy

    'Modify Fillet Bead1
     boolstatus = swFeat.ModifyDefinition(swWeldBead, swModel, Nothing)

End Sub
```
