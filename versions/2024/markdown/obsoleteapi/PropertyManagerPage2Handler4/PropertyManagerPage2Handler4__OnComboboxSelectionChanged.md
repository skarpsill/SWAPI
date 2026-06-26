---
title: "PropertyManagerPage2Handler4::OnComboboxSelectionChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnComboboxSelectionChanged.htm"
---

# PropertyManagerPage2Handler4::OnComboboxSelectionChanged

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler5::OnComboboxSelectionChanged.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnComboboxSelectionChanged.htm)

Description

This method is called when
a user changes the selected item in a combo box on this PropertyManager.

Syntax (OLE Autom

void = PropertyManagerPage2Handler4.OnComboboxSelectionChanged
( Id, Item )

(Table)=========================================================

| Input: | (long) Id | ID of the combo box |
| --- | --- | --- |
| Input: | (long) Item | ID of the item |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnComboboxSelectionChanged
( Id, Item )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Id | ID of the combo box |
| --- | --- | --- |
| Input: | (long) Item | ID of the item |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

If the user can edit the text
in the text box, then use this method with PropertyManagerPagew2Handler4::OnComboxEditChanged
tokadov_tag{{<spaces>}}kadov_tag{{</spaces>}}find
out what is in the text box of the combo box.

When this method is called,
the control may not yet be updated with the current selection, so the
PropertyManagerPageCombobox::CurrentSelection property is not reliable.
To get the current text, use the value of Item that is passed into the
method as the argument to PropertyManagerPageCombobox::ItemText.

If the user has edited the
text in the text box and then clicks the arrow to show or hide the list
box of the combo box, and the text in the text box matches the first characters
in any of the items in the list, then that item is automatically selected
in the list and this method is called, indicating that the selected item
has changed.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnComboboxSelectionChanged.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="PropertyManagerPage2Handler4_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnComboboxSelectionChanged.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
