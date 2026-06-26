---
title: "Deselect Marked Entity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Deselect_Marked_Entity_Example_VB.htm"
---

# Deselect Marked Entity Example (VBA)

This example shows how to deselect a previously selected and marked entity.

```
'--------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the Base-Extrude feature.
' 2. Examine the graphics area and FeatureManager
'    design tree to verify.
' 3. At Stop, press F5 to continue.
' 4. Deselects the Base-Extrude feature.
' 5. Examine the Immediate window, graphics
'    area, and FeatureManager design tree to verify.
'-------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelExt As SldWorks.ModelDocExtension
Dim bRet As Boolean
Dim lMark As Long
Dim lMarkedIdx As Long
Dim lNumMarkedSelections As Long
Dim lNumAllSelections As Long
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
    ' Open the document
    Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt")
    Set swModel = swApp.ActiveDoc
    If swModel Is Nothing Then
        Set swModel = swApp.OpenDoc7(swDocSpecification)
    End If
```

```
    Set swSelMgr = swModel.SelectionManager
    Set swModelExt = swModel.Extension
    ' Select the Base-Extrude feature and mark with a value of 8
    bRet = swModelExt.SelectByID2("Base-Extrude", "BODYFEATURE", 0, 0, 0, False, 8, Nothing, swSelectOptionDefault)
```

```
    Stop
    ' Examine the part to verify that Base-Extrude was selected
    ' Press F5 to continue
```

```
    ' Look for a given mark value
        lMark = 8
        ' Get the number of marked selections
        lNumMarkedSelections = swSelMgr.GetSelectedObjectCount2(lMark)
        Debug.Print "Number of marked selections = " & lNumMarkedSelections
```

```
        ' Get the total number of selections
        lNumAllSelections = swSelMgr.GetSelectedObjectCount2(-1)
        Debug.Print "Number of selections        = " & lNumAllSelections
```

```
        Debug.Print " "
```

```
         ' Deselect the marked selection
         For lMarkedIdx = 1 To lNumAllSelections
            Debug.Print ("Selected object #" & lMarkedIdx & " deselected? " & swSelMgr.DeSelect2(lMarkedIdx, lMark))
         Next lMarkedIdx

         ' Examine the graphics area to verify that Base-Extrude is deselected
```

```
End Sub
```
