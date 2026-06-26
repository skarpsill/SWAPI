---
title: "PropertyManagerPage2Handler4::OnPreview"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnPreview.htm"
---

# PropertyManagerPage2Handler4::OnPreview

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler5::OnPreview.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnPreview.htm)

Description

This method is called when
a user clicks the Preview button on a PropertyManager page.

Syntax (OLE Automation)

retval = PropertyManagerPage2Handler4.OnPreview ()

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if the operations specified
by your add-in executes, FALSE if not (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnPreview
( &retval)

Parameters Table Start

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if the operations specified by your add-in
executes, FALSE if not (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

To show a Preview button on
a PropertyManager page, include swPropertyManagerOptions_PreviewButton
in the Options argument of SldWorks::CreatePropertyManagerPage.

You can do whatever you want
in response to the Preview button being clicked. Your add-in is responsible
for preview handling, including keeping track of the state of the Preview
button. Your add-in controls what happens when the Preview button is clicked;
SolidWorks takes not action when the Preview button is clicked. SolidWorks
ignores the return value because by the time the callback handler is called,
the button has already changed.

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
<param name="Items" value="ZReleaseNotes005plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnPreview.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnPreview.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
