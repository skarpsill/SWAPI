---
title: "Get Dispatch Objects for Selection Set Items Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dispatch_Objects_for_Selection_Set_Items_Example_VB.htm"
---

# Get Dispatch Objects for Selection Set Items Example (VBA)

This example shows how to get the Dispatch objects for selection set items.

```
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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionSet1 As SldWorks.SelectionSet
Dim swSelectionSet2 As SldWorks.SelectionSet
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Sub TraverseFeatureFeatures(swFeat As SldWorks.Feature, swModel As SldWorks.ModelDoc2)
    Dim swSelectionSetFolder As SldWorks.SelectionSetFolder
    Dim selectionSetArray As Variant
    Dim selectionSetItemArray As Variant
    Dim selectionSetItemArrayTypes As Variant
    Dim swSelectionSet As SldWorks.SelectionSet
    Dim swSelectionSetItem As SldWorks.SelectionSetItem
    Dim swFace As SldWorks.Face2
    Dim swEdge As SldWorks.Edge
    Dim swBody As SldWorks.Body2
    Dim i As Long
    Dim j As Long
```

```
    While Not swFeat Is Nothing
        If swFeat.name = "Selection Sets" Then
            Debug.Print "    " & swFeat.name & " [" & swFeat.GetTypeName & "]"
            'Get Selection Sets folder
            Set swSelectionSetFolder = swFeat.GetSpecificFeature2
            'Get selection sets in Selection Sets folder
            selectionSetArray = swSelectionSetFolder.GetSelectionSets
            For i = 0 To UBound(selectionSetArray)
                Set swSelectionSet = selectionSetArray(i)
                Debug.Print "      Selection set[" & i & "] name: " & swSelectionSet.GetName
                'Get the items and their types in this selection set
                selectionSetItemArray = swSelectionSet.GetSelectionSetItems
                selectionSetItemArrayTypes = swSelectionSet.GetSelectionSetItemTypes
                For j = 0 To UBound(selectionSetItemArray)
                    Set swSelectionSetItem = selectionSetItemArray(j)
                    Select Case selectionSetItemArrayTypes(j)
                        Case swSelectType_e.swSelFACES
                            'Get the Dispatch object for the selection set item
                            Set swFace = swSelectionSetItem.GetCorrespondingItem
                            'Get the name of the body for the face
                            Set swBody = swFace.GetBody
                            Debug.Print "        Name of face[" & j & "]'s body: " & swBody.name
                        Case swSelectType_e.swSelEDGES
                            'Get the Dispatch object for the selection set item
                            Set swEdge = swSelectionSetItem.GetCorrespondingItem
                            'Get the name of the body for the edge
                            Set swBody = swEdge.GetBody
                            Debug.Print "        Name of edge[" & j & "]'s body: " & swBody.name
                        End Select
                Next
            Next
        End If
        Set swFeat = swFeat.GetNextFeature
    Wend
End Sub
```

```
Sub TraverseModelFeatures(swModel As SldWorks.ModelDoc2)
    Dim swFeat As SldWorks.Feature
```

```
    Set swFeat = swModel.FirstFeature
    TraverseFeatureFeatures swFeat, swModel
End Sub
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Create a selection set
    status = swModelDocExt.SelectByID2("", "FACE", -2.32252739277783E-02, -2.48041260152831E-02, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -2.58449612883283E-02, -6.28596853454155E-03, -7.49999999999318E-03, True, 0, Nothing, 0)
     Set swSelectionSet1 = swModelDocExt.SaveSelection(errors)
    Debug.Print "  First selection set created (1 = succeeded; 0 = failed)? " & errors
    swModel.ClearSelection2 True
```

```
    'Create another selection set
    status = swModelDocExt.SelectByID2("", "EDGE", 2.97500073491506E-02, -6.96186204362448E-03, -7.3680822854385E-03, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 2.99025466658236E-02, -1.99243068692567E-02, -3.6983143110092E-03, True, 0, Nothing, 0)
    Set swSelectionSet2 = swModelDocExt.SaveSelection(errors)
    Debug.Print "  Second selection set created (1 = succeeded; 0 = failed)? " & errors
    swModel.ClearSelection2 True
```

```
    'Traverse the model to get Selection Sets folder
    TraverseModelFeatures swModel
```

```
End Sub
```
