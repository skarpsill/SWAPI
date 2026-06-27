---
title: "Insert Join Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Join_Feature_Example_VBNET.htm"
---

# Insert Join Feature Example (VB.NET)

This example shows how to insert a join feature.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Verify that c:\temp exists.
' 3. Verify that c:\temp\Part1^arm2.sldprt does not exist. If it does,
'    delete or drag it to a different folder.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Edits the assembly, selects a face, and inserts a new part.
' 3. Selects the components for the join feature and inserts a
'    join feature, which is a feature of Part1^arm2<1> in the
'    the FeatureManager design tree.
' 4. Accesses the join feature
' 5. Gets the number of joined components.
' 6. Iterates through the components, prints the name of
'    each component, and, if an Inplace mate, prints
'    its mate component names and Inplace mate types.
' 7. Examine the Immediate window, FeatureManager design tree, and
'    the graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swAssemblyDoc As AssemblyDoc
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFace As Face2
        Dim swSketchManager As SketchManager
        Dim swFeature As Feature
        Dim swJoinFeatureData As JoinFeatureData
        Dim swSelObj As Object
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim info As Integer
        Dim state As Integer
        Dim swComponent As Component2
        Dim singleComponent As Object
        Dim components() As Object
        Dim mates() As Object
        Dim singleMate As Object
        Dim swMate As Mate2
        Dim swMateInPlace As MateInPlace
        Dim numMateEntities As Integer
        Dim typeOfMate As Integer
        Dim i As Integer

        'Open assembly document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\arm2.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swAssemblyDoc = swModel

        'Edit the assembly, select a face, and insert a new part
        swAssemblyDoc.EditPart2(True, False, info)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", 0.0102799485791252, 0.00285108269579837, -0.00454660000001184, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFace = swSelectionMgr.GetSelectedObject6(1, -1)
        swSelObj = swFace
        state = swAssemblyDoc.InsertNewPart2("C:\temp\Part1^arm2.sldprt", swSelObj)
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swModel.EditUndo2(1)

        'Select the components for the join feature and insert a join feature
        status = swModelDocExt.SelectByID2("secondGrip-1@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("pincap-1@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("pincap-4@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("pincap-5@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("pincap-6@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swAssemblyDoc.InsertJoin2(True, False)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Join1@Part1^arm2-1@arm2", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)

        'Access the join feature, which is a feature of Part1^arm2<1> in the
        'the FeatureManager design tree
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swJoinFeatureData = swFeature.GetDefinition
        swJoinFeatureData.AccessSelections(swModel, Nothing)

        'Get the number of joined components
        Debug.Print("Number of joined components: " & swJoinFeatureData.GetJoinedPartsCount)

        swFeature.ReleaseSelectionAccess()
```

```
        Debug.Print("")

        'Get components
        components = swAssemblyDoc.GetComponents(False)
        For Each singleComponent In components
            swComponent = singleComponent
            'Print name of component
            Debug.Print("Name of component: " & swComponent.Name2)
            'Get mates
            mates = swComponent.GetMates()
            If Not mates Is Nothing Then
                For Each singleMate In mates
                    'Get mate type
                    If TypeOf singleMate Is Mate2 Then
                        swMate = singleMate
                        typeOfMate = swMate.Type
                    End If
                    'If Inplace mate, print mate component name and Inplace mate type
                    If TypeOf singleMate Is MateInPlace Then
                        swMateInPlace = singleMate
                        numMateEntities = swMateInPlace.GetMateEntityCount
                        For i = 0 To numMateEntities - 1
                            Debug.Print("  Mate component name: " & swMateInPlace.MateComponentName(i))
                            Debug.Print("    Type of Inplace mate: " & swMateInPlace.MateEntityType(i))
                        Next i
                    End If
                Next
            End If
            Debug.Print("")
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
