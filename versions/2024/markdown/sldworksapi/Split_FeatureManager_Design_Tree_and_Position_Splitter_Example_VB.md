---
title: "Split FeatureManager Design Tree and Position Splitter Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_VB.htm"
---

# Split FeatureManager Design Tree and Position Splitter Example (VBA)

This example shows how:

- to split a FeatureManager design tree.
- add a tab to one of the FeatureManager design trees.
- change the location of the split panel bar (splitter).

```
'----------------------------------------------------------
' Preconditions:
' 1. In the IDE:
'    a. Reference your ActiveX control file (click Tools >
'       References > Browse > browse to the folder where the
'       ActiveX control file resides and click the ActiveX
'       control file > Open > OK).
'    a. Insert the ActiveX component (click Insert > Components >
'       ActiveX component's check box > OK).
' 2. Verify that the specified part document and bitmap exist.
' 3. Replace activex_control_component_declaration and
'    activex_control_CLSID_or_ProgID with your ActiveX control's
'    information.
'
' Postconditions:
' 1. Opens the part document and splits the FeatureManager
'    design tree; the splitter is below the FeatureManager
'    design tree to which the tab was added. Drag the splitter
'    to verify.
' 2. Close the part document.
' 3. Set test to 1 in the macro.
' 4. Rerun the macro.
' 5. Opens the part document and splits the FeatureManager
'    design tree; the splitter is above the FeatureManager
'    design tree to which the tab was added. Drag the
'    splitter to verify.
'
' NOTE: Because the part document is used elsewhere,
' do not save changes.
'----------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
    Const iconSmall As String = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\user macro icons\button.bmp"
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModViewMgr As SldWorks.ModelViewManager
    Dim swFeatMgrTabTop As SldWorks.FeatMgrView
    Dim swFeatMgrTabBtm As SldWorks.FeatMgrView
    Dim ctrlTop As activex_control_component_declaration
    Dim ctrlBtm As activex_control_component_declaration
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim activePane As Long
    Dim test As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModViewMgr = swModel.ModelViewManager
```

```
    test = 0
```

```
    If test = 0 Then
        ' FeatureManager design tree is split, and the splitter is
        ' below the FeatureManager design tree to which the
        ' tab was added
        Set swFeatMgrTabTop = swModViewMgr.CreateFeatureMgrControl2(iconSmall, "activex_control_CLSID_or_ProgID", "", "Top tab ToolTip", swFeatMgrPaneTop)
        Set ctrlTop = swFeatMgrTabTop.GetControl
        swModel.FeatureManagerSplitterPosition = 0#
        activePane = swFeatMgrTabTop.ActivateView
    Else
        ' FeatureManager design tree is split, and the splitter is
        ' above the FeatureManager design tree to which the
        ' tab was added
        Set swFeatMgrTabBtm = swModViewMgr.CreateFeatureMgrControl2(iconSmall, "activex_control_CLSID_or_ProgID", "", "Bottom tab ToolTip", swFeatMgrPaneBottom)
        Set ctrlBtm = swFeatMgrTabBtm.GetControl
        swModel.FeatureManagerSplitterPosition = 1#
        activePane = swFeatMgrTabBtm.ActivateView
    End If
```

```
End Sub
```
