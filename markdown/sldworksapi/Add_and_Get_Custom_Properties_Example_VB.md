---
title: "Add and Get Custom Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Get_Custom_Properties_Example_VB.htm"
---

# Add and Get Custom Properties Example (VBA)

This example shows how to add and get a custom property assigned to a weldment feature.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
' 2. Select the Weldment feature in the FeatureManager design
'    tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Adds a custom property named Date added to the selected
'    weldment feature.
' 2. To verify:
'    * Examine the Immediate window.
'    * Right-click the Weldment feature in the FeatureManager
'      design and click Properties.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'-------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swCustPropMgr As SldWorks.CustomPropertyManager
    Dim nRetVal As Long
    Dim vNameArr As Variant
    Dim vName As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, 0)
    Set swCustPropMgr = swFeat.CustomPropertyManager
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name & " [" & swFeat.GetTypeName & "]"
```

```
    ' Add custom property
    nRetVal = swCustPropMgr.Add3("Date added", swCustomInfoType_e.swCustomInfoDate, "17-Apr-2005", swCustomPropertyAddOption_e.swCustomPropertyDeleteAndAdd)
```

```
    ' Get all custom properties
    vNameArr = swCustPropMgr.GetNames: If IsEmpty(vNameArr) Then Exit Sub
    For Each vName In vNameArr
        Debug.Print "    " & vName & " [" & swCustPropMgr.GetType(vName) & "] = " & swCustPropMgr.Get(vName)
    Next vName
```

```
End Sub
```
