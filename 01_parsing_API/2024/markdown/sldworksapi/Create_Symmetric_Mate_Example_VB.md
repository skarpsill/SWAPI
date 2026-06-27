---
title: "Create and Edit Symmetric Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Symmetric_Mate_Example_VB.htm"
---

# Create and Edit Symmetric Mate Example (VBA)

This example shows how to create and edit a symmetric mate.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo3.sldasm
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a symmetric mate.
 ' 2. Press F5 to continue.
 ' 3. Changes the symmetry plane and the entities to mate.
 ' 4. Inspect the Immediate window and graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim boolstatus As Boolean
 Dim face As SldWorks.Face2
 Dim AsmDoc As SldWorks.AssemblyDoc
 Dim MateData As SldWorks.MateFeatureData
 Dim SymmMateData As SldWorks.SymmetricMateFeatureData
 Dim selman As SelectionMgr
 Dim FaceVar As Variant
 Dim Feat As SldWorks.Feature
 Dim Plane As Object
 Dim EntToMate As Variant
 Dim FaceArr(1) As SldWorks.Face2
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set AsmDoc = swModel

    Set MateData = AsmDoc.CreateMateData(8) 'Symmetric mate
    Set selman = swModel.SelectionManager

    ' Set the symmetry plane
     Set Plane = AsmDoc.FeatureByName("Front Plane")
     MateData.SymmetryPlane = Plane

    ' Select the faces
     boolstatus = swModel.Extension.SelectByRay(-0.119833719900839, 0.14832954277739, -1.38999787131979E-02, -0.638789958006775, -0.241329918931549, -0.730552708418903, 1.94730543661126E-03, 2, False, 0, 0)
     boolstatus = swModel.Extension.SelectByRay(5.98755999561718E-03, 4.37101841503704E-02, -1.38999787133685E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 9.54271027477843E-04, 2, True, 0, 0)

    ' Set the entities to mate
     Set FaceArr(0) = selman.GetSelectedObject6(1, -1)
     Set FaceArr(1) = selman.GetSelectedObject6(2, -1)
    FaceVar = FaceArr
     MateData.EntitiesToMate = FaceVar

    MateData.MateAlignment = 1
    Set Feat = AsmDoc.CreateMate(MateData)

    swModel.GraphicsRedraw2

    Stop

    Set Feat = swModel.Extension.GetLastFeatureAdded
     Debug.Print "Feature type of mate created is " & Feat.GetTypeName2

    Set MateData = Feat.GetDefinition

    swModel.ClearSelection2 (True)

    Set SymmMateData = MateData

    Set Plane = AsmDoc.FeatureByName("Top Plane")
     SymmMateData.SymmetryPlane = Plane

    boolstatus = swModel.Extension.SelectByRay(-0.122740690662738, 0.149346213190292, -8.00800212867898E-02, -0.640294734796254, 5.58893693642409E-02, 0.766093356572332, 2.43053632782351E-03, 2, False, 0, 0)
     boolstatus = swModel.Extension.SelectByRay(5.98755999561718E-03, 4.37101841503704E-02, -1.38999787133685E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 9.54271027477843E-04, 2, True, 0, 0)
    Set FaceArr(0) = selman.GetSelectedObject6(1, -1)
     Set FaceArr(1) = selman.GetSelectedObject6(2, -1)

    FaceVar = FaceArr

    SymmMateData.EntitiesToMate = FaceVar

    Debug.Print "Symmetric mate alignment is " & SymmMateData.MateAlignment

    Call Feat.ModifyDefinition(SymmMateData, swModel, Nothing)
End Sub
```
