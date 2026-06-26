---
title: "Split FeatureManager Design Tree and Position Splitter Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_VBNET.htm"
---

# Split FeatureManager Design Tree and Position Splitter Example (VB.NET)

This example shows how:

- to split a FeatureManager design tree.
- add a tab to one of the FeatureManager design trees.
- change the location of the split panel bar (splitter).

```vb
 '----------------------------------------------------------
 ' Preconditions:
 ' 1. In the IDE, reference your ActiveX control file
 '    (click Project > Add Reference > Browse and browse
 '    to the folder where the ActiveX control resides and click
 '    the ActiveX control file > OK).
 ' 2. Verify that the specified part document and bitmap exist.
 ' 3. Replace activex_control_component_declaration and
 '    activex_control_CLSID_or_ProgID with your ActiveX control's
 '    information.
 '
 ' Postconditions:
 ' 1. Opens the part document and splits the FeatureManager design
 '    tree; the splitter is below the FeatureManager design tree
 '    to which the   tab was added. Drag the splitter to verify.
 ' 2. Close the part document.
 ' 3. Set test to 1 in the macro.
 ' 4. Rerun the macro.
 ' 5.  Opens the part document and splits the FeatureManager design
 '    tree; the splitter is  above the FeatureManager design tree
 '    to which the   tab was added. Drag the splitter to verify.
 '
 ' NOTE: Because the part document is used elsewhere,
 ' do not save changes.
 '----------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst

 Partial Class SolidWorksMacro

     Public Sub Main()

         Const iconSmall As String = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\user macro icons\button.bmp"

         Dim swModel As ModelDoc2
         Dim swModViewMgr As ModelViewManager
         Dim swFeatMgrTabTop As FeatMgrView
         Dim swFeatMgrTabBtm As FeatMgrView
         Dim ctrlTop As  activex_control_component_declaration
         Dim ctrlBtm As  activex_control_component_declaration
         Dim fileName As String
         Dim errors As Integer
         Dim warnings As Integer
         Dim activePane As Integer
         Dim test As Integer

         fileName =  "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModViewMgr = swModel.ModelViewManager

         test = 0

         If test = 0 Then
             ' FeatureManager design tree is split, and the splitter is
             ' below the FeatureManager design tree to which the
             ' tab was added
             swFeatMgrTabTop = swModViewMgr.CreateFeatureMgrControl2(iconSmall, "activex_control_CLSID_or_ProgID", "", "Top tab ToolTip", swFeatMgrPane_e.swFeatMgrPaneTop)
             ctrlTop = swFeatMgrTabTop.GetControl
             swModel.FeatureManagerSplitterPosition = 0.0#
             activePane = swFeatMgrTabTop.ActivateView
         Else
             ' FeatureManager design tree is split, and the splitter is
             ' above the FeatureManager design tree to which the
             ' tab was added
             swFeatMgrTabBtm = swModViewMgr.CreateFeatureMgrControl2(iconSmall, "activex_control_CLSID_or_ProgID", "", "Bottom tab ToolTip", swFeatMgrPane_e.swFeatMgrPaneBottom)
             ctrlBtm = swFeatMgrTabBtm.GetControl
             swModel.FeatureManagerSplitterPosition = 1.0#
             activePane = swFeatMgrTabBtm.ActivateView
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End  Class
```
