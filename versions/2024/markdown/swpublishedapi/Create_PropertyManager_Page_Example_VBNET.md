---
title: "Create PropertyManager Page Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Create_PropertyManager_Page_Example_VBNET.htm"
---

# Create PropertyManager Page Example (VB.NET)

This example shows how to create a PropertyManager
page that contains the following controls:

- ActiveX
- Bitmap
- Bitmap button
- Button
- Combo box
- Group box
- Label
- List box
- Number box
- Radio button
- Selection box
- Slider
- Tab

This
example also shows how to handle focus events for these controls.

NOTE:If the model is an assembly
that contains multiple components, and you want to allow the user to
select edges, faces, or vertices, then you must specify swSelCOMPSDONTOVERRIDE
for parameter SelType of IPropertyManagerPageSelectionbox::SetSelectionFilters.
Otherwise, if the user attempts to select an edge, face, or vertex, then the
entire component might get selected and not the edge, face, or vertex. This
example demonstrates how to specify SelType.

```vb
'----------------------------------------------------------------------------
 '    Preconditions:
 ' 1. Copy  Modules - main to your project.
 ' 2. Copy  Class Modules - clsPropMgr to a class in your project.
 ' 3. Right-click the name of your project, select
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Add Reference, browse install_dir\api\redist\, select
 '    SolidWorks.Interop.swpublished.dll, and click OK.
  ' 4. Ensure that the specified assembly document exists.
 ' 5. Modify ClassID and LicenseKey parameters in
 '    IPropertyManagerPageActiveX::SetClass to add your ActiveX control
 '    to the PropertyManager page.
 ' 6. Open an Immediate window.
 '
 '   Postconditions:
 ' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Creates a PropertyManager page called Comps.
 ' 2. Creates the specified controls.
 ' 3. kadov_tag{{</spaces>}}Inspect the contents of Comps and the Immediate Window as
 '  kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}you use the controls. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
 ' 4. Click the green check mark to close the PropertyManager page.
 '
 ' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}NOTES:
 ' *kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}After running this macro, select
 ' kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Tools > Options > System Options > Stop VSTA debugger
 ' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}on macro exit.
 ' kadov_tag{{<spaces>}} * kadov_tag{{</spaces>}}Because the assembly document is used elsewhere,
 '   do not save any changes when closing the document.
 '----------------------------------------------------------------------------
 'Modules - main
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Part As ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents pm As clsPropMgr

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openDocErrors As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim OpenDocWarnings As Integer

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, False)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bladed shaft.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", openDocErrors, OpenDocWarnings)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Create a new instance of the PropertyManager class
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pm = New clsPropMgr(swApp)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pm.Show()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```

[Back to top](#Top)

```vb
 'Class Modules - clsPropMgr
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swpublished
Imports System
Imports System.Runtime.InteropServices
Imports System.Diagnostics

<ComVisibleAttribute(True)> _
Public Class clsPropMgr

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Implements  PropertyManagerPage2Handler9

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swApp As SldWorks
     'Control objects required for the PropertyManager page
     Dim pm_Page As PropertyManagerPage2
     Dim pm_Group As PropertyManagerPageGroup
     Dim pm_Selection As PropertyManagerPageSelectionbox
     Dim pm_Selection2 As PropertyManagerPageSelectionbox
     Dim pm_Label As PropertyManagerPageLabel
     Dim pm_Combo As PropertyManagerPageCombobox
     Dim pm_List As PropertyManagerPageListbox
     Dim pm_Number As PropertyManagerPageNumberbox
     Dim pm_Radio As PropertyManagerPageOption
     Dim pm_Slider As PropertyManagerPageSlider
     Dim pm_Tab As PropertyManagerPageTab
     Dim pm_Button As PropertyManagerPageButton
     Dim pm_BMPButton As PropertyManagerPageBitmapButton
     Dim pm_Bitmap As PropertyManagerPageBitmap
     Dim pm_ActiveX As PropertyManagerPageActiveX

     'Each control in the page needs a unique ID
     Const GroupID As Integer = 1
     Const LabelID As Integer = 2
     Const SelectionID As Integer = 3
     Const ComboID As Integer = 4
     Const ListID As Integer = 5
     Const Selection2ID As Integer = 6
     Const NumberID As Integer = 7
     Const RadioID As Integer = 8
     Const SliderID As Integer = 9
     Const TabID As Integer = 10
     Const ButtonID As Integer = 11
     Const BMPButtonID As Integer = 12
     Const BitmapID As Integer = 13
     Const ActiveXID As Integer = 14

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim ClickedCancel As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim retVal As Integer

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub Show()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pm_Page.Show2(0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'The following runs when a new instance
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'of the class is created
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub New(ByVal swApp As SldWorks)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim PageTitle As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim caption As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim tip As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim options As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim longerrors As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim controlType As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim alignment As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim listItems(3) As String

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Set the variables for the page
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}PageTitle = "Comps"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}options = swPropertyManagerButtonTypes_e.swPropertyManager_OkayButton _
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}+ swPropertyManagerButtonTypes_e.swPropertyManager_CancelButton _
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}+ swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage _
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}+ swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Create the PropertyManager page
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pm_Page = CType(swApp.CreatePropertyManagerPage(PageTitle, _
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}options, Me, longerrors), PropertyManagerPage2)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Make sure that the page was created properly
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If longerrors = swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay Then

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}'Add the controls to the page
             'Add a tab
             pm_Tab = pm_Page.AddTab(TabID, "Application", "", 0)

             'Add a group box to the tab
             caption = "Controls"
             options = swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + _
                 swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded
             pm_Group = pm_Tab.AddGroupBox(GroupID, caption, options)

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}'Add two selection boxes
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}controlType = swPropertyManagerPageControlType_e.swControlType_Selectionbox
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}caption = "" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}' No caption for selection boxes
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}options = swAddControlOptions_e.swControlOptions_Visible + _
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swAddControlOptions_e.swControlOptions_Enabled
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}tip = "Select an edge, face, vertex, solid body, or a component"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection = pm_Group.AddControl2(SelectionID, _
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}controlType, caption, alignment, options, tip)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection2 = pm_Group.AddControl2(Selection2ID, _
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}controlType, caption, alignment, options, tip)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim filters(6) As swSelectType_e
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}filters(0) = swSelectType_e.swSelEDGES
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}filters(1) = swSelectType_e.swSelREFEDGES
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}filters(2) = swSelectType_e.swSelFACES
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}filters(3) = swSelectType_e.swSelVERTICES
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}filters(4) = swSelectType_e.swSelSOLIDBODIES
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}filters(5) = swSelectType_e.swSelCOMPONENTS
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}filters(6) = swSelectType_e.swSelCOMPSDONTOVERRIDE
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim filterObj As Object
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}filterObj = filters
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection.SingleEntityOnly = False
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection.AllowMultipleSelectOfSameEntity = True
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection.Height = 50
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection.SetSelectionFilters(filterObj)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection2.SingleEntityOnly = False
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection2.AllowMultipleSelectOfSameEntity = True
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection2.Height = 50
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Selection2.SetSelectionFilters(filterObj)

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}'Add a combo box
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}controlType = swPropertyManagerPageControlType_e.swControlType_Combobox
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}caption = ""
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}options = swAddControlOptions_e.swControlOptions_Visible + _
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swAddControlOptions_e.swControlOptions_Enabled

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}tip = "Select a value"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Combo = pm_Group.AddControl2(ComboID, _
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}controlType, caption, alignment, options, tip)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If Not pm_Combo Is Nothing Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Combo.Height = 50
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}listItems(0) = "Value 1"
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}listItems(1) = "Value 2"
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}listItems(2) = "Value 3"
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}listItems(3) = "Value 4"
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Combo.AddItems(listItems)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Combo.CurrentSelection = 0
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}'Add a list box
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}controlType = swPropertyManagerPageControlType_e.swControlType_Listbox
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}caption = ""
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}alignment = swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}options = swAddControlOptions_e.swControlOptions_Visible + _
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swAddControlOptions_e.swControlOptions_Enabled
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}tip = "Multi-select values in the list box"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_List = pm_Group.AddControl2(ListID, _
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}controlType, caption, alignment, options, tip)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_List.Style = swPropMgrPageListBoxStyle_e.swPropMgrPageListBoxStyle_MultipleItemSelect
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_List.Height = 50
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If Not pm_List Is Nothing Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_List.Height = 50
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}listItems(0) = "Value 1"
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}listItems(1) = "Value 2"
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}listItems(2) = "Value 3"
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}listItems(3) = "Value 4"
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_List.AddItems(listItems)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_List.SetSelectedItem(1, True)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If

             'Add a label
             pm_Label = pm_Group.AddControl2(LabelID, swPropertyManagerPageControlType_e.swControlType_Label, "Label", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "")

             'Add a slider
             pm_Slider = pm_Group.AddControl2(SliderID, swPropertyManagerPageControlType_e.swControlType_Slider, "Slider", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Slide")

             'Add a radio button
             pm_Radio = pm_Group.AddControl2(RadioID, swPropertyManagerPageControlType_e.swControlType_Option, "Radio button", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Select")

             'Add a number box
             pm_Number = pm_Group.AddControl2(NumberID, swPropertyManagerPageControlType_e.swControlType_Numberbox, "Number box", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Spin")

             'Add a button
             pm_Button = pm_Group.AddControl2(ButtonID, swPropertyManagerPageControlType_e.swControlType_Button, "Button", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Click")

             'Add a bitmap button
             pm_BMPButton = pm_Group.AddControl2(BMPButtonID, swPropertyManagerPageControlType_e.swControlType_BitmapButton, "Bitmap button", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Click")
             pm_BMPButton.SetStandardBitmaps(swPropertyManagerPageBitmapButtons_e.swBitmapButtonImage_parallel)

             'Add a bitmap
             pm_Bitmap = pm_Group.AddControl2(BitmapID, swPropertyManagerPageControlType_e.swControlType_Bitmap, "Bitmap", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Bitmap")
             pm_Bitmap.SetStandardBitmap(swBitmapControlStandardTypes_e.swBitmapControl_Volume)

             'Add an ActiveX control
             pm_ActiveX = pm_Group.AddControl2(ActiveXID, swPropertyManagerPageControlType_e.swControlType_ActiveX, "ActiveX", swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "ActiveX control tip")
             pm_ActiveX.SetClass("ClassID", "LicenseKey")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else kadov_tag{{<spaces>}}

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("An error occurred while attempting to create the PropertyManager Page", vbCritical)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub AfterActivation() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.AfterActivation
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub AfterClose() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.AfterClose
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function OnActiveXControlCreated(ByVal Id As Integer, ByVal Status As Boolean) As Integer Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnActiveXControlCreated
         Debug.Print("ActiveX control created")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnButtonPress(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnButtonPress
         Debug.Print("Button clicked")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnCheckboxCheck(ByVal Id As Integer, ByVal Checked As Boolean) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnCheckboxCheck
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnClose(ByVal Reason As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnClose
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Cancel Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}'Cancel button clicked
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ClickedCancel = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ElseIf Reason = swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}'OK button clicked
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ClickedCancel = False
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnComboboxEditChanged(ByVal Id As Integer, ByVal Text As String) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnComboboxEditChanged
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnComboboxSelectionChanged(ByVal Id As Integer, ByVal Item As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnComboboxSelectionChanged
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnGainedFocus(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnGainedFocus
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim varArray As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Control box " & Id & " gained focus")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}varArray = pm_List.GetSelectedItems
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pm_Combo.CurrentSelection = varArray(0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnGroupCheck(ByVal Id As Integer, ByVal Checked As Boolean) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnGroupCheck
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnGroupExpand(ByVal Id As Integer, ByVal Expanded As Boolean) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnGroupExpand
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function OnHelp() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnHelp
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function OnKeystroke(ByVal Wparam As Integer, ByVal Message As Integer, ByVal Lparam As Integer, ByVal Id As Integer) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnKeystroke
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnListboxSelectionChanged(ByVal Id As Integer, ByVal Item As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnListboxSelectionChanged
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnLostFocus(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnLostFocus
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Control box " & Id & " lost focus")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function OnNextPage() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnNextPage
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnNumberboxChanged(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnNumberboxChanged
         Debug.Print("Number box changed")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnOptionCheck(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnOptionCheck
         Debug.Print ("Option selected")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnPopupMenuItem(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPopupMenuItem
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnPopupMenuItemUpdate(ByVal Id As Integer, ByRef retval As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPopupMenuItemUpdate
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function OnPreview() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPreview
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function OnPreviousPage() As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnPreviousPage
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnRedo() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnRedo
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnSelectionboxCalloutCreated(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSelectionboxCalloutCreated
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnSelectionboxCalloutDestroyed(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSelectionboxCalloutDestroyed
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnSelectionboxFocusChanged(ByVal Id As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSelectionboxFocusChanged
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("The focus moved to selection box " & Id)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnSelectionboxListChanged(ByVal Id As Integer, ByVal Count As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSelectionboxListChanged
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pm_Page.SetCursor(swPropertyManagerPageCursors_e.swPropertyManagerPageCursors_Advance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("The list in selection box " & Id & " changed")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnSliderPositionChanged(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSliderPositionChanged
         Debug.Print("Slider position changed")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnSliderTrackingCompleted(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSliderTrackingCompleted
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function OnSubmitSelection(ByVal Id As Integer, ByVal Selection As Object, ByVal SelType As Integer, ByRef ItemText As String) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnSubmitSelection
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Return True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Function OnTabClicked(ByVal Id As Integer) As Boolean Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnTabClicked
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnTextboxChanged(ByVal Id As Integer, ByVal Text As String) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnTextboxChanged
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnUndo() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnUndo
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub OnWhatsNew() Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnWhatsNew
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

    Public Sub OnListBoxRMBUp(ByVal Id As Integer, ByVal posX As Integer, ByVal posY As Integer) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnListboxRMBUp
    End Sub

    Public Function OnWindowFromHandleControlCreated(ByVal Id As Integer, ByVal Status As Boolean) As Integer Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnWindowFromHandleControlCreated
    End Function

    Public Sub OnNumberBoxTrackingCompleted(ByVal Id As Integer, ByVal Value As Double) Implements SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.OnNumberBoxTrackingCompleted

    End Sub
End Class
```

[Back to top](#Top)
