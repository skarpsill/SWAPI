---
title: "Get Dispatch Objects for Selection Set Items Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dispatch_Objects_for_Selection_Set_Items_Example_VBNET.htm"
---

# Get Dispatch Objects for Selection Set Items Example (VB.NET)

```
This example shows how to get the Dispatch objects for selection set items.

'-------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects two faces and creates a selection set.
' 3. Selects two edges and creates a selection set.
' 4. Traverses the FeatureManager design tree. If the feature is the
'    Selection Sets folder, then:
'    a. Gets its name.
'    b. Gets each selection set in the Selection Sets folder.
'       1. Gets the selection set items and their types.
'       2. Gets the Dispatch object for each selection set item.
'       3. Gets the name of the body for each selection set item.
' 5. Examine the Immediate window and FeatureManager design tree.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionSet1 As SelectionSet
        Dim swSelectionSet2 As SelectionSet
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Create a selection set
        status = swModelDocExt.SelectByID2("", "FACE", -0.0232252739277783, -0.0248041260152831, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0258449612883283, -0.00628596853454155, -0.00749999999999318, True, 0, Nothing, 0)
        swSelectionSet1 = swModelDocExt.SaveSelection(errors)
        Debug.Print("  First selection set created (1 = succeeded; 0 = failed)? " & errors)
        swModel.ClearSelection2(True)

        'Create another selection set
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0297500073491506, -0.00696186204362448, -0.0073680822854385, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0299025466658236, -0.0199243068692567, -0.0036983143110092, True, 0, Nothing, 0)
        swSelectionSet2 = swModelDocExt.SaveSelection(errors)
        Debug.Print("  Second selection set created (1 = succeeded; 0 = failed)? " & errors)
        swModel.ClearSelection2(True)

        'Traverse the model to get the Selection Sets folder
        TraverseModelFeatures(swModel)

    End Sub

    Sub TraverseFeatureFeatures(ByVal swFeat As Feature, ByVal swModel As ModelDoc2)
        Dim swSelectionSetFolder As SelectionSetFolder
        Dim selectionSetArray As Object
        Dim selectionSetItemArray As Object
        Dim selectionSetItemArrayTypes As Object
        Dim swSelectionSet As SelectionSet
        Dim swSelectionSetItem As SelectionSetItem
        Dim swFace As Face2
        Dim swEdge As Edge
        Dim swBody As Body2
        Dim i As Integer
        Dim j As Integer
        Dim selectionSetItemArrayType As Integer

        While Not swFeat Is Nothing
            If swFeat.name = "Selection Sets" Then
                Debug.Print("    " & swFeat.name & " [" & swFeat.GetTypeName & "]")
                'Get Selection Sets folder
                swSelectionSetFolder = swFeat.GetSpecificFeature2
                'Get selection sets in Selection Sets folder
                selectionSetArray = swSelectionSetFolder.GetSelectionSets
                For i = 0 To UBound(selectionSetArray)
                    swSelectionSet = selectionSetArray(i)
                    Debug.Print("      Selection set[" & i & "] name: " & swSelectionSet.GetName)
                    'Get the items and their types in this selection set
                    selectionSetItemArray = swSelectionSet.GetSelectionSetItems
                    selectionSetItemArrayTypes = swSelectionSet.GetSelectionSetItemTypes
                    For j = 0 To UBound(selectionSetItemArray)
                        swSelectionSetItem = selectionSetItemArray(j)
                        selectionSetItemArrayType = selectionSetItemArrayTypes(j)
                        Select Case selectionSetItemArrayType
                            Case swSelectType_e.swSelFACES
                                'Get the Dispatch object for the selection set item
                                swFace = swSelectionSetItem.GetCorrespondingItem
                                'Get the name of the body for the face
                                swBody = swFace.GetBody
                                Debug.Print("        Name of face[" & j & "]'s body: " & swBody.Name)
                            Case swSelectType_e.swSelEDGES
                                'Get the Dispatch object for the selection set item
                                swEdge = swSelectionSetItem.GetCorrespondingItem
                                'Get the name of the body for the edge
                                swBody = swEdge.GetBody
                                Debug.Print("        Name of edge[" & j & "]'s body: " & swBody.Name)
                        End Select
                    Next
                Next
            End If
            swFeat = swFeat.GetNextFeature
        End While
    End Sub

    Sub TraverseModelFeatures(ByVal swModel As ModelDoc2)
        Dim swFeat As Feature
        swFeat = swModel.FirstFeature
        TraverseFeatureFeatures(swFeat, swModel)
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
