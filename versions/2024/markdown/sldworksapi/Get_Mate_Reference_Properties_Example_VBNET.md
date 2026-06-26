---
title: "Get Mate Reference Properties Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mate_Reference_Properties_Example_VBNET.htm"
---

# Get Mate Reference Properties Example (VB.NET)

This example shows how to get mate reference properties.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Inserts a mate reference.
' 3. Gets properties of the mate reference.
' 4. Examine the FeatureManager design tree and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Sub main()

        Dim swMateReference As MateReference
        Dim swFeature As Feature
        Dim mateRefObj As Object
        Dim mateRefEntityType As Long
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swPlane As Entity
        Dim swFeatureMgr As FeatureManager
        Dim strMateReferencename As String
        Dim nCount As Integer
        Dim refEntType As Integer
        Dim mateRefAlignment As Integer
        Dim boolstatus As Boolean
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        swModel = swApp.ActiveDoc
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Insert mate reference
        boolstatus = swModelDocExt.SelectByID2("Front", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        swPlane = swSelMgr.GetSelectedObject6(1, -1)
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00835786916030656, 0.00429540237419701, 0, True, 2, Nothing, 0)
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.InsertMateReference2("Default", Nothing, 0, 1, False, Nothing, 0, 2, False, Nothing, 0, 0)
        swModel.ClearSelection2(True)
        boolstatus = swModelDocExt.SelectByID2("Default-<1>", "POSGROUP", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelMgr.GetSelectedObject6(1, -1)
        swMateReference = swFeature.GetSpecificFeature2

        swModel.ClearSelection2(True)

        ' Get the name of the mate reference
        strMateReferencename = swMateReference.Name
        Debug.Print("Name of mate reference = " & strMateReferencename)

        ' Get the number of reference entities in the mate reference
        nCount = swMateReference.ReferenceEntityCount
        Debug.Print("Number of mate reference entities = " & nCount)

        ' Get the mate reference type for the primary mate
        ' entity in the selected mate reference
        refEntType = swMateReference.ReferenceType(0)
        Debug.Print("Mating type of primary mate entity = " & refEntType)

        ' Get the mate reference alignment for the
        ' mate reference entity in the selected mate reference
        mateRefAlignment = swMateReference.ReferenceAlignment(0)
        Debug.Print("Alignment of primary mate entity = " & mateRefAlignment)

        ' Get the  mate reference entity in the mate reference
        mateRefObj = swMateReference.ReferenceEntity2(0)

        ' Get the mate reference entity type
        mateRefEntityType = swMateReference.ReferenceEntityType(0)
        Debug.Print("Entity type of primary mate entity = " & mateRefEntityType)

        ' QueryInterface the returned object as a face, if a face
        If mateRefEntityType = swSelectType_e.swSelFACES Then
            Dim mateRefFace As Face2
            mateRefFace = mateRefObj
            Debug.Print("Primary mate entity is a face with area = " & mateRefFace.GetArea)
        End If

        swModel.ClearSelection2(True)

    End Sub

    Public swApp As SldWorks

End Class
```
