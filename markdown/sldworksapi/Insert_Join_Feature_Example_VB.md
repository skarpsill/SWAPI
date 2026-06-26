---
title: "Insert Join Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Join_Feature_Example_VB.htm"
---

# Insert Join Feature Example (VBA)

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
'    each component, and if an Inplace mate,
'    prints its mate component names and Inplace mate types.
' 7. Examine the Immediate window, FeatureManager design tree, and
'    the graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swAssemblyDoc As SldWorks.AssemblyDoc
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFace As SldWorks.Face2
Dim swSketchManager As SldWorks.SketchManager
Dim swFeature As SldWorks.Feature
Dim swJoinFeatureData As SldWorks.JoinFeatureData
Dim swSelObj As Object
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim info As Long
Dim state As Long
Dim swComponent As SldWorks.Component2
Dim singleComponent As Variant
Dim components As Variant
Dim mates As Variant
Dim singleMate As Variant
Dim swMate As SldWorks.Mate2
Dim swMateInPlace As SldWorks.MateInPlace
Dim numMateEntities As Long
Dim typeOfMate As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open assembly document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\arm2.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swAssemblyDoc = swModel
```

```
    'Edit the assembly, select a face, and insert a new part
    swAssemblyDoc.EditPart2 True, False, info
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", 1.02799485791252E-02, 2.85108269579837E-03, -4.54660000001184E-03, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFace = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swSelObj = swFace
    state = swAssemblyDoc.InsertNewPart2("C:\temp\Part1^arm2.sldprt", swSelObj)
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    swModel.EditUndo2 1
```

```
    'Select the components for the join feature and insert a join feature
    status = swModelDocExt.SelectByID2("secondGrip-1@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("pincap-1@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("pincap-4@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("pincap-5@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("pincap-6@arm2", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swAssemblyDoc.InsertJoin2(True, False)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Join1@Part1^arm2-1@arm2", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
```

```
    'Access the join feature, which is a feature of Part1^arm2<1> in the
    'the FeatureManager design tree
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swJoinFeatureData = swFeature.GetDefinition
    swJoinFeatureData.AccessSelections swModel, Nothing
```

```
    'Get the number of joined components
    Debug.Print "Number of joined components: " & swJoinFeatureData.GetJoinedPartsCount

    swJoinFeatureData.ReleaseSelectionAccess

    Debug.Print ""
```

```
    'Get components
    components = swAssemblyDoc.GetComponents(False)
    For Each singleComponent In components
        Set swComponent = singleComponent
        'Print name of component
        Debug.Print "Name of component: " & swComponent.Name2
        'Get mates
        mates = swComponent.GetMates()
        If (Not IsEmpty(mates)) Then
            For Each singleMate In mates
                  'Get mate type
                  If TypeOf singleMate Is SldWorks.Mate2 Then
                    Set swMate = singleMate
                    typeOfMate = swMate.Type
                End If
                'If Inplace mate, print mate component name and Inplace mate type
                If TypeOf singleMate Is SldWorks.MateInPlace Then
                    Set swMateInPlace = singleMate
                    numMateEntities = swMateInPlace.GetMateEntityCount
                    For i = 0 To numMateEntities - 1
                        Debug.Print "  Mate component name: " & swMateInPlace.MateComponentName(i)
                        Debug.Print "    Type of Inplace mate: " & swMateInPlace.MateEntityType(i)
                    Next i
                End If
            Next
        End If
        Debug.Print ""
    Next
```

```
End Sub
```
