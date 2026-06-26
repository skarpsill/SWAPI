---
title: "Create PropertyManager Page Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Create_PropertyManager_Page_Example_CSharp.htm"
---

# Create PropertyManager Page Example (C#)

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
//-------------------------------------------------------------------------
 // Preconditions:
 // 1 kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Copy  Modules - Main to your project.
 // 2. Copy  Class Modules - clsPropMgr to a class in your project.
 // 3. Right-click the name of your project, select
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Add Reference, browse install_dir\api\redist\, select
 //    SolidWorks.Interop.swpublished.dll, and click OK.
 // 4. Ensure that the namespace and class names in the sample code
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}match that of your C# project.
  // 5. Ensure that the specified assembly document exists.
 // 6. Modify ClassID and LicenseKey parameters in
 //    IPropertyManagerPageActiveX::SetClass to add your ActiveX control
 //    to the PropertyManager page.
 // 7. Open an Immediate window.
 //
 // Postconditions:
 // kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1. Creates a PropertyManager page called Comps.
 // 2. Creates the specified controls.
 // 3. kadov_tag{{</spaces>}}Inspect the contents of Comps and the Immediate Window as
 //  kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}you use the controls. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
 // 4. Click the green check mark to close the PropertyManager page.
 //
 // NOTES:
 // kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}* kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}After running this macro, select
 // kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Tools > Options > System Options > Stop VSTA debugger
 //   kadov_tag{{</spaces>}}on macro exit.
 // kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}* kadov_tag{{</spaces>}}Because the assembly document is used elsewhere,
 //   do not save kadov_tag{{</spaces>}}any changes when closing the document.
 //---------------------------------------------------------------------------
//  Modules - Main
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace CreatePropertyManagerPageExample_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public ModelDoc2 Part;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public clsPropMgr pm;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int openDocErrors = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int openDocWarnings = 0;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, false);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bladed shaft.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref openDocErrors, ref openDocWarnings);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Create a new instance of the PropertyManager class
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm = new clsPropMgr(swApp);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm.Show();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
```

}

[Back to top](#Top)

```vb
//  Class Modules - clsPropMgr
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swpublished;
using System;
using System.Runtime.InteropServices;
using System.Diagnostics;
namespace CreatePropertyManagerPageExample_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}[ComVisibleAttribute(true)]
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public class clsPropMgr : PropertyManagerPage2Handler9
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}
          //Control objects required for the PropertyManager page
         PropertyManagerPage2 pm_Page;
         PropertyManagerPageGroup pm_Group;
         PropertyManagerPageSelectionbox pm_Selection;
         PropertyManagerPageSelectionbox pm_Selection2;
         PropertyManagerPageLabel pm_Label;
         PropertyManagerPageCombobox pm_Combo;
         PropertyManagerPageListbox pm_List;
         PropertyManagerPageNumberbox pm_Number;
         PropertyManagerPageOption pm_Radio;
         PropertyManagerPageSlider pm_Slider;
         PropertyManagerPageTab pm_Tab;
         PropertyManagerPageButton pm_Button;
         PropertyManagerPageBitmapButton pm_BMPButton;
         PropertyManagerPageBitmap pm_Bitmap;
         PropertyManagerPageActiveX pm_ActiveX;

         //Each control in the page needs a unique ID
         const int GroupID = 1;
         const int LabelID = 2;
         const int SelectionID = 3;
         const int ComboID = 4;
         const int ListID = 5;
         const int Selection2ID = 6;
         const int NumberID = 7;
         const int RadioID = 8;
         const int SliderID = 9;
         const int TabID = 10;
         const int ButtonID = 11;
         const int BMPButtonID = 12;
         const int BitmapID = 13;
         const int ActiveXID = 14;

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Show()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Page.Show2(0);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//The following runs when a new instance
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//of the class is created
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public clsPropMgr(SldWorks swApp)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string PageTitle = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string caption = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string tip = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long options = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int longerrors = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int controlType = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int alignment = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string[] listItems = new string[4];

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Set the variables for the page
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PageTitle = "Comps";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}options = (int)swPropertyManagerButtonTypes_e.swPropertyManager_OkayButton + (int)swPropertyManagerButtonTypes_e.swPropertyManager_CancelButton + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_LockedPage + (int)swPropertyManagerPageOptions_e.swPropertyManagerOptions_PushpinButton;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Create the PropertyManager page
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Page = (PropertyManagerPage2)swApp.CreatePropertyManagerPage(PageTitle, (int)options, this, ref longerrors);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Make sure that the page was created properly
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (longerrors == (int)swPropertyManagerPageStatus_e.swPropertyManagerPage_Okay)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}//Add the controls to the page

                  //Add a tab
          pm_Tab = pm_Page.AddTab(TabID, "Application", "", 0);

          //Add a group box to the tab
          caption = "Controls";
          options = (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Visible + (int)swAddGroupBoxOptions_e.swGroupBoxOptions_Expanded;
          pm_Group = (PropertyManagerPageGroup)pm_Tab.AddGroupBox(GroupID, caption, options);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}
 //Add two selection boxes
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}controlType = (int)swPropertyManagerPageControlType_e.swControlType_Selectionbox;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}caption = "";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}alignment = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}tip = "Select an edge, face, vertex, solid body, or a component";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection = (PropertyManagerPageSelectionbox)pm_Group.AddControl2(SelectionID, (short)controlType, caption, (short)alignment, (int)options, tip);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection2 = (PropertyManagerPageSelectionbox)pm_Group.AddControl2(Selection2ID, (short)controlType, caption, (short)alignment, (int)options, tip);

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swSelectType_e[] filters = new swSelectType_e[7];
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}filters[0] = swSelectType_e.swSelEDGES;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}filters[1] = swSelectType_e.swSelREFEDGES;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}filters[2] = swSelectType_e.swSelFACES;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}filters[3] = swSelectType_e.swSelVERTICES;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}filters[4] = swSelectType_e.swSelSOLIDBODIES;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}filters[5] = swSelectType_e.swSelCOMPONENTS;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}filters[6] = swSelectType_e.swSelCOMPSDONTOVERRIDE;

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}object filterObj = null;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}filterObj = filters;

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection.SingleEntityOnly = false;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection.AllowMultipleSelectOfSameEntity = true;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection.Height = 50;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection.SetSelectionFilters(filterObj);

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection2.SingleEntityOnly = false;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection2.AllowMultipleSelectOfSameEntity = true;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection2.Height = 50;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Selection2.SetSelectionFilters(filterObj);

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}//Add a combo box
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}controlType = (int)swPropertyManagerPageControlType_e.swControlType_Combobox;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}caption = "";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}alignment = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}tip = "Select a value";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_Combo = (PropertyManagerPageCombobox)pm_Group.AddControl2(ComboID, (short)controlType, caption, (short)alignment, (int)options, tip);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if ((pm_Combo != null))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}pm_Combo.Height = 50;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}listItems[0] = "Value 1";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}listItems[1] = "Value 2";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}listItems[2] = "Value 3";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}listItems[3] = "Value 4";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}pm_Combo.AddItems(listItems);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}pm_Combo.CurrentSelection = 0;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}//Add a list box
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}controlType = (int)swPropertyManagerPageControlType_e.swControlType_Listbox;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}caption = "";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}alignment = (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_Indent;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}options = (int)swAddControlOptions_e.swControlOptions_Visible + (int)swAddControlOptions_e.swControlOptions_Enabled;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}tip = "Multi-select values in the list box";
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pm_List = (PropertyManagerPageListbox)pm_Group.AddControl2(ListID, (short)controlType, caption, (short)alignment, (int)options, tip);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if ((pm_List != null))
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}pm_List.Style = (int)swPropMgrPageListBoxStyle_e.swPropMgrPageListBoxStyle_MultipleItemSelect;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}pm_List.Height = 50;
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}listItems[0] = "Value 1";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}listItems[1] = "Value 2";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}listItems[2] = "Value 3";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}listItems[3] = "Value 4";
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}pm_List.AddItems(listItems);
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}pm_List.SetSelectedItem(1, true);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
                 //Add a label
         pm_Label = (PropertyManagerPageLabel)pm_Group.AddControl2(LabelID, (int)swPropertyManagerPageControlType_e.swControlType_Label, "Label", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "");

         //Add a slider
         pm_Slider = (PropertyManagerPageSlider)pm_Group.AddControl2(SliderID, (int)swPropertyManagerPageControlType_e.swControlType_Slider, "Slider", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Slide");

         //Add a radio button
         pm_Radio = (PropertyManagerPageOption)pm_Group.AddControl2(RadioID, (int)swPropertyManagerPageControlType_e.swControlType_Option, "Radio button", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Select");

         //Add a number box
         pm_Number = (PropertyManagerPageNumberbox)pm_Group.AddControl2(NumberID, (int)swPropertyManagerPageControlType_e.swControlType_Numberbox, "Number box", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Spin");

         //Add a button
         pm_Button = (PropertyManagerPageButton)pm_Group.AddControl2(ButtonID, (int)swPropertyManagerPageControlType_e.swControlType_Button, "Button", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Click");

         //Add a bitmap button
         pm_BMPButton = (PropertyManagerPageBitmapButton)pm_Group.AddControl2(BMPButtonID, (int)swPropertyManagerPageControlType_e.swControlType_BitmapButton, "Bitmap button", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Click");
         pm_BMPButton.SetStandardBitmaps((int)swPropertyManagerPageBitmapButtons_e.swBitmapButtonImage_parallel);

         //Add a bitmap
         pm_Bitmap = (PropertyManagerPageBitmap)pm_Group.AddControl2(BitmapID, (int)swPropertyManagerPageControlType_e.swControlType_Bitmap, "Bitmap", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "Bitmap");
         pm_Bitmap.SetStandardBitmap((int)swBitmapControlStandardTypes_e.swBitmapControl_Volume);

         //Add an ActiveX control
         pm_ActiveX = (PropertyManagerPageActiveX)pm_Group.AddControl2(ActiveXID, (int)swPropertyManagerPageControlType_e.swControlType_ActiveX, "ActiveX", (int)swPropertyManagerPageControlLeftAlign_e.swControlAlign_LeftEdge, options, "ActiveX control tip");
         pm_ActiveX.SetClass("ClassID", "LicenseKey");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}//If the page is not created
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("An error occurred while attempting to create the " + "PropertyManager Page");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

#region  IPropertyManagerPage2Handler9 Members
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.AfterActivation()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        }
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.AfterClose()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int IPropertyManagerPage2Handler9.OnActiveXControlCreated(int Id, bool Status)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("ActiveX control created");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnButtonPress(int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
             Debug.Print("Button clicked");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnCheckboxCheck(int Id, bool Checked)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnClose(int Reason)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (Reason == (int)swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Cancel)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}//Do something when the cancel button is clicked
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else if (Reason == (int)swPropertyManagerPageCloseReasons_e.swPropertyManagerPageClose_Okay)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}//Do something else when the OK button is clicked
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnComboboxEditChanged(int Id, string Text)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnComboboxSelectionChanged(int Id, int Item)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnGainedFocus(int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}short[] varArray = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Control box " + Id + " gained focus");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}varArray = (short[])pm_List.GetSelectedItems();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Combo.CurrentSelection = varArray[0];
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnGroupCheck(int Id, bool Checked)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnGroupExpand(int Id, bool Expanded)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool IPropertyManagerPage2Handler9.OnHelp()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        }
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool IPropertyManagerPage2Handler9.OnKeystroke(int Wparam, int Message, int Lparam, int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnListboxSelectionChanged(int Id, int Item)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnLostFocus(int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Control box " + Id + " lost focus");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool IPropertyManagerPage2Handler9.OnNextPage()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnNumberboxChanged(int Id, double Value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            Debug.Print("Number box changed");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnOptionCheck(int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            Debug.Print("Option selected");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnPopupMenuItem(int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnPopupMenuItemUpdate(int Id, ref int retval)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool IPropertyManagerPage2Handler9.OnPreview()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool IPropertyManagerPage2Handler9.OnPreviousPage()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnRedo()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnSelectionboxCalloutCreated(int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnSelectionboxCalloutDestroyed(int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnSelectionboxFocusChanged(int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("The focus moved to selection box " + Id);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnSelectionboxListChanged(int Id, int Count)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pm_Page.SetCursor((int)swPropertyManagerPageCursors_e.swPropertyManagerPageCursors_Advance);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("The list in selection box " + Id + " changed");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnSliderPositionChanged(int Id, double Value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Slider position changed");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnSliderTrackingCompleted(int Id, double Value)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool IPropertyManagerPage2Handler9.OnSubmitSelection(int Id, object Selection, int SelType, ref string ItemText)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
// This method must return true for selections to occur
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return true;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool IPropertyManagerPage2Handler9.OnTabClicked(int Id)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnTextboxChanged(int Id, string Text)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnUndo()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}void IPropertyManagerPage2Handler9.OnWhatsNew()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
         void IPropertyManagerPage2Handler9.OnListboxRMBUp(int Id, int PosX, int PosY)
         {

         }
```

```vb
   int IPropertyManagerPage2Handler9.OnWindowFromHandleControlCreated(int Id, bool Status)
    {

    }
   void IPropertyManagerPage2Handler9.OnNumberBoxTrackingCompleted(int Id, double Value)
    {

    }
```

```vb
        #endregion
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```

[Back to top](#Top)
