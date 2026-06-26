---
title: "Modify Fillet Weld Bead Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Fillet_Weld_Bead_Example_VBNET.htm"
---

# Modify Fillet Weld Bead Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim swSelMgr As SelectionMgr
     Dim swWeldBead As WeldmentBeadFeatureData
     Dim swFeat As Feature
     Dim swSelData As SelectData
     Dim v1 As Vertex
     Dim v2 As Vertex
     Dim set1 As Object
     Dim faceVar As Object
     Dim ve As Object
     Dim fVar1 As Object
     Dim fVar2 As Object
     Dim f1(0) As Object
     Dim f2(1) As Object
     Dim e(0) As Object
     Dim bdlen As Double
     Dim bdPitch As Double
     Dim bdsz As Double
     Dim bdTy As Integer
     Dim i As Integer
     Dim boolstatus As Boolean

     Sub main()

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swSelMgr = swModel.SelectionManager
         swSelData = swSelMgr.CreateSelectData

         'Select Fillet Bead1 feature
         boolstatus = swModelDocExt.SelectByID2("Fillet Bead1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swWeldBead = swFeat.GetDefinition

         'Roll back to the feature just before Fillet Bead1
         boolstatus = swWeldBead.AccessSelections(swModel, Nothing)

         'Get Fillet Bead1 properties
         Debug.Print("Fillet Bead1 properties:")
         bdlen = swWeldBead.BeadLength(swWeldBeadSide_e.swWeldBeadArrowSide)
         Debug.Print("  Weld bead length: " & bdlen)

         bdPitch = swWeldBead.BeadPitch(swWeldBeadSide_e.swWeldBeadArrowSide)
         Debug.Print("  Weld bead pitch: " & bdPitch)

         bdsz = swWeldBead.BeadSize(swWeldBeadSide_e.swWeldBeadArrowSide)
         Debug.Print("  Weld bead size: " & bdsz)

         bdTy = swWeldBead.BeadType(swWeldBeadSide_e.swWeldBeadArrowSide)
         Debug.Print("  Weld bead type as defined in swWeldBeadType_e: " & bdTy)

         Debug.Print("  Propagate the weld bead along the tangent? " & swWeldBead.TangentPropagation)
         Debug.Print("  Apply weld bead to both sides of intersecting faces? " & swWeldBead.UseOtherSide)

         'Get Fillet Bead1 faces
         swWeldBead.GetFaces(swWeldBeadSide_e.swWeldBeadArrowSide, set1, faceVar)

         For i = LBound(faceVar) To UBound(faceVar)
             faceVar(i).Select4(True, swSelData)
         Next i

         For i = LBound(set1) To UBound(set1)
             set1(i).Select4(True, swSelData)
         Next i

         'Get Fillet Bead1 virtual edges
         ve = swWeldBead.GetVirtualEdges(False, swWeldBeadSide_e.swWeldBeadArrowSide)

         For i = LBound(ve) To UBound(ve)
             boolstatus = ve(i).Select4(True, swSelData)
             v1 = ve(i).GetStartVertex
             v2 = ve(i).GetEndVertex
         Next i

         swModel.ClearSelection2(True)

         'Set new properties of Fillet Bead1
         swWeldBead.BeadLength(swWeldBeadSide_e.swWeldBeadArrowSide) = bdlen * 0.5
         swWeldBead.BeadPitch(swWeldBeadSide_e.swWeldBeadArrowSide) = bdPitch * 0.5
         swWeldBead.BeadSize(swWeldBeadSide_e.swWeldBeadArrowSide) = bdsz * 0.5
         swWeldBead.BeadType(swWeldBeadSide_e.swWeldBeadArrowSide) = bdTy

         'Modify Fillet Bead1
         boolstatus = swFeat.ModifyDefinition(swWeldBead, swModel, Nothing)

     End Sub

     Public swApp As SldWorks

 End Class
```
