---
title: "Delete and Insert Instances in Variable Pattern Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VB.htm"
---

# Delete and Insert Instances in Variable Pattern Feature Example (VBA)

This example shows how to delete and insert instances in a variable pattern feature.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\bottle.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the variable pattern feature.
' 2. Rolls back and accesses the variable pattern feature.
'    a. Deletes the last instance of the variable pattern in the table.
'    b. Deletes a dimension in the table.
'    c. Gets the names of the controlling dimensions.
'    d. Inserts a new instance in the table.
'    e. Rolls forward the variable pattern feature.
'       NOTE: It can take several minutes for this step to complete.
' 3. Selects the variable pattern again.
'    a. Rolls back and accesses the variable pattern feature.
'    b. Sets new values for the new instance.
'    c. Rolls forward the variable pattern feature.
' 4. Examine the Immediate window and graphics area.
'
' NOTE: Because the part is used elsewhere, do not save change.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swDimensionDrivenTablePatternFeat As SldWorks.DimPatternFeatureData
Dim status As Boolean
Dim DimensionName As String
Dim errorString As String
Dim i As Long
```

```
Sub main()
    Set swApp = Application.SldWorks
```

```
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    status = swModelDocExt.SelectByID2("VarPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swDimensionDrivenTablePatternFeat = swFeature.GetDefinition
```

```
    'Roll back and access the variable pattern feature
    status = swDimensionDrivenTablePatternFeat.AccessSelections(swModel, Nothing)
```

```
    'Delete the last instance of the variable pattern in the table
    status = swDimensionDrivenTablePatternFeat.DeleteInstanceAt(-1)
    Debug.Print "Last instance of variable pattern deleted from table? " & status
```

```
    'Delete a dimension in the table
    DimensionName = "D3@Fillet1"
    status = swDimensionDrivenTablePatternFeat.DeleteDimension(DimensionName)
    Debug.Print "D3@Fillet1 dimension deleted from table? " & status
```

```
    'Get the names of the controlling dimensions
    Dim nbr As Long
    Dim dimNbr As Long
    Dim controllingDimNames() As String
    Dim controllingDimName As String
    nbr = swDimensionDrivenTablePatternFeat.GetInstanceCount
    Debug.Print ("Number of pattern instances: " & nbr)
    Debug.Print ("  Controlling dimension names: ")
    dimNbr = swDimensionDrivenTablePatternFeat.GetControllingDimensionCount
    ReDim Preserve controllingDimNames(dimNbr)
    For i = 0 To dimNbr - 1
       controllingDimNames(i) = swDimensionDrivenTablePatternFeat.GetControllingDimensionName(i)
       controllingDimName = controllingDimNames(i)
       Debug.Print ("     " & controllingDimName)
    Next i
```

```
    'Insert instance in table
    status = swDimensionDrivenTablePatternFeat.AddInstanceAt(False, -1)
    Debug.Print "Instance added to table? " & status
    nbr = swDimensionDrivenTablePatternFeat.GetInstanceCount
    Debug.Print ("Number of pattern instances: " & nbr)
```

```
    'Roll forward the variable pattern feature
    'NOTE: It can several minutes for this step to complete.
    swFeature.ModifyDefinition swDimensionDrivenTablePatternFeat, swModel, Nothing
```

```
    'Select the variable pattern again
    status = swModelDocExt.SelectByID2("VarPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swDimensionDrivenTablePatternFeat = swFeature.GetDefinition
```

```
    'Roll back and access the variable pattern feature
    status = swDimensionDrivenTablePatternFeat.AccessSelections(swModel, Nothing)
```

```
    'Set new values for the new instance
    errorString = swDimensionDrivenTablePatternFeat.SetInstanceDimensionValue(nbr, "D3@Sketch2@bottle.moPart_c", 0.15)
    If errorString = "" Then
        Debug.Print "Set new value for new instance[" & nbr & "] D3@Sketch2 dimension? True"
    Else
        Debug.Print "Set new value for new instance[" & nbr & "] D3@Sketch2 dimension? " & errorString
    End If
    errorString = swDimensionDrivenTablePatternFeat.SetInstanceDimensionValue(nbr, "D1@Fillet1@bottle.moPart_c", 0.01)
    If errorString = "" Then
        Debug.Print "Set new value for new instance[" & nbr & "] D2Fillet2 dimension? True"
    Else
        Debug.Print "Set new value for new instance[" & nbr & "] D2Fillet2 dimension? " & errorString
    End If
```

```
    'Roll forward the variable pattern feature
    swFeature.ModifyDefinition swDimensionDrivenTablePatternFeat, swModel, Nothing
```

```
End Sub
```
