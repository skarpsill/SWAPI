---
title: "Get Objects in Selection Set Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Objects_in_Selection_Set_Example_VBNET.htm"
---

# Get Objects in Selection Set Example (VB.NET)

This example shows how to get the objects in a selection set.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Verify that the assembly to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Creates two selection sets.
' 3. Traverses the nodes in the FeatureManager design tree. If the
'    name of the node is Selection-Set1(3), then:
'    a. Gets the type of feature for this node.
'    b. Gets the Selection Sets folder.
'    c. Gets the selection set by name.
'    d. Suspends the current selection list, starts a new selection list,
'       and adds the objects in the selection set to the new selection
'       list.
'    e. Gets the number of objects in the selection list and traverses
'       the selection list.
'       1. Gets the type of object in the selection list.
'       2. Casts the object to a component.
'       3. Gets the name of the component.
'    f. Reinstates the suspended selection list.
' 4. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'----------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swFeatureMgr As FeatureManager
        Dim rootNode As TreeControlItem
        Dim swModelDocExtension As ModelDocExtension
        Dim swSelectionSet1 As SelectionSet
        Dim swSelectionSet2 As SelectionSet
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\wrench.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        Debug.Print("File = " & swModel.GetPathName)
        swModelDocExtension = swModel.Extension

        'Create a selection set
        status = swModelDocExtension.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("clamp2-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        swSelectionSet1 = swModelDocExtension.SaveSelection(errors)
        swModel.ClearSelection2(True)

        'Create another selection set
        status = swModelDocExtension.SelectByID2("centerlink-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionSet2 = swModelDocExtension.SaveSelection(errors)
        swModel.ClearSelection2(True)

        swFeatureMgr = swModel.FeatureManager
        rootNode = swFeatureMgr.GetFeatureTreeRootItem()
        If Not rootNode Is Nothing Then
            traverse_node(rootNode, swFeatureMgr, swModel)
        End If

    End Sub

    Private Sub traverse_node(ByVal node As TreeControlItem, ByVal swFeatureMgr As FeatureManager, ByVal swModel As ModelDoc2)
        Dim childNode As TreeControlItem
        Dim featureNode As Feature
        Dim nodeObjectType As Integer
        Dim nodeObject As Object

        nodeObjectType = node.ObjectType
        nodeObject = node.Object
        Select Case nodeObjectType
            Case swTreeControlItemType_e.swFeatureManagerItem_Feature
                If Not nodeObject Is Nothing Then
                    featureNode = nodeObject
                    If featureNode.Name = "Selection-Set1(3)" Then

                        Dim swSelectionSetFeature As Feature
                        Dim swSelectionSetFolderFeature As SelectionSetFolder
                        Dim swSelectionSet As SelectionSet
                        Dim swComponent As Component2
                        Dim swSelectionMgr As SelectionMgr
                        Dim nbrSelections As Integer
                        Dim i As Integer
                        Dim selObj As Object

                        swSelectionSetFeature = node.Object
                        Debug.Print("Feature name: " & swSelectionSetFeature.Name)
                        Debug.Print("  Feature type: " & swSelectionSetFeature.GetTypeName2)
                        swSelectionSetFolderFeature = swFeatureMgr.GetSelectionSetFolder
                        swSelectionSet = swSelectionSetFolderFeature.GetSelectionSetByName(swSelectionSetFeature.Name)
                        Debug.Print("Selection set name: " & swSelectionSet.GetName)

                        swSelectionMgr = swModel.SelectionManager
                        swSelectionMgr.SuspendSelectionList()

                        swSelectionSet.Select()

                        nbrSelections = swSelectionMgr.GetSelectedObjectCount2(-1)
                        Debug.Print("  Number of objects selected in this selection set: " & nbrSelections)
                        For i = 1 To nbrSelections
                            'Get each object in the new selection list
                            selObj = swSelectionMgr.GetSelectedObject6(i, -1)
                            Debug.Print("    Object[" & i & "] in the selection list is of swSelectType_e = " & swSelectionMgr.GetSelectedObjectType3(i, -1) & "")
                            'Cast the object
                            swComponent = selObj
                            Debug.Print("       Name of component: " & swComponent.Name2)
                        Next

                        swSelectionMgr.ResumeSelectionList()
                    End If
                End If

        End Select

        childNode = node.GetFirstChild()
        While Not childNode Is Nothing
            traverse_node(childNode, swFeatureMgr, swModel)
            childNode = childNode.GetNext
        End While

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
