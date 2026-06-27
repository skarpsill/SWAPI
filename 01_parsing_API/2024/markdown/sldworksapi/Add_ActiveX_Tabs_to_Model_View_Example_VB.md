---
title: "Add ActiveX Tabs to Model View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_ActiveX_Tabs_to_Model_View_Example_VB.htm"
---

# Add ActiveX Tabs to Model View Example (VBA)

This example shows how to add two ActiveX tabs to a model view.

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
' 2. Verify that the specified part document exists.
' 3. Replace activex_control_component_declaration and
'    activex_control_CLSID_or_ProgID with your ActiveX control's
'    information.
'
' Postconditions:
' 1. Opens the part document and adds two new tabs to the model view.
' 2. Activates the model view.
' 3. To verify the ActiveX controls on the new tabs,
'    click each tab.
'
' NOTE: Because the part document is used elsewhere,
' do not save changes.
'------------------------------------------------------------
```

```
Option Explicit
```

```
Sub Main()
```

```
    Const calTabName1 As String = "Tab 1"
    Const calTabName2 As String = "Tab 2"
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModViewMgr As SldWorks.ModelViewManager
    Dim calCtrl1 As activex_control_component_declaration
    Dim calCtrl2 As activex_control_component_declaration
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim status  As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModViewMgr = swModel.ModelViewManager
```

```
    ' Add the ActiveX control tabs
    Set calCtrl1 = swModViewMgr.AddControl(calTabName1, "activex_control_CLSID_or_ProgID", "")
    Set calCtrl2 = swModViewMgr.AddControl(calTabName2, "activex_control_CLSID_or_ProgID", "")
```

```
    status = swModViewMgr.ActivateControlTab(calTabName1)
    status = swModViewMgr.IsControlTabActive(calTabName1)
    status = swModViewMgr.IsModelTabActive
```

```
    ' Switch back to model view
    status = swModViewMgr.ActivateModelTab
```

```
End Sub
```
