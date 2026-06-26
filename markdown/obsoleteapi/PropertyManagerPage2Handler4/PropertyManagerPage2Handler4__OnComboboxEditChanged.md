---
title: "PropertyManagerPage2Handler4::OnComboboxEditChanged"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnComboboxEditChanged.htm"
---

# PropertyManagerPage2Handler4::OnComboboxEditChanged

This method is obsolete and has been superseded
by P[ropertyManagerPage2Handler5::OnComboboxEditChanged.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnComboboxEditChanged.htm)

Description

This method is called when
a user changes the text string in the text box of a combo box.

Syntax (OLE Automation)

void = PropertyManagerPage2Handler4.OnComboboxEditChanged
( Id, Text )

(Table)=========================================================

| Input: | (long) Id | ID of the combo box |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnComboboxEditChanged
( Id, Text )

Parameters Table Start

(Table)=========================================================

| Input: | (long) Id | ID of combo box |
| --- | --- | --- |
| Input: | (BSTR) Text | Text string |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is only called
if the combo box was set up as an editable text box. If the combo box
is set up to as a static text box, then this method is not called.

If the user can edit the text
in the text box, then use this method with PropertyManagerPage2Handler4::OnComboxSelectionChanged
to find out what is in the text box of the combo box.

When this method is called,
the control may not yet be updated with the current selection, so the
PropertyManagerPageCombobox::CurrentSelection property is not reliable.
The text passed into this method is the up-to-date text.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZReleaseNotes2003$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnComboboxEditChanged.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnComboboxEditChanged.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
