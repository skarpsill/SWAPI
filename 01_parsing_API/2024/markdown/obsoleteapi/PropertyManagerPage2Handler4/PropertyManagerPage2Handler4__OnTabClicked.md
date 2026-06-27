---
title: "PropertyManagerPage2Handler4::OnTabClicked"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PropertyManagerPage2Handler4/PropertyManagerPage2Handler4__OnTabClicked.htm"
---

# PropertyManagerPage2Handler4::OnTabClicked

This method is obsolete and has been superseded
by[PropertyManagerPage2Handler5::OnTabClicked.](sldworksAPI.chm::/PropertyManagerPage2Handler5/PropertyManagerPage2Handler5__OnTabClicked.htm)

Description

This method is called when
a user clicks a tab on a multi-tab PropertyManager page.

Syntax (OLE Automation)

retval = PropertyManagerPage2Handler4.OnTabClicked
( Id)

(Table)=========================================================

| Input: | (long) Id | ID of the tab clicked (see Remarks ) |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the tab clicked is processed,
FALSE if not |

Syntax (COM)

status = PropertyManagerPage2Handler4->OnTabClicked
( Id, &retval)

Parameters Table Start

(Table)=========================================================

| Input: | (long) Id | ID of the tab clicked (see Remarks ) |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the tab clicked is processed,
FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The value of Id is the ID
that was specified when the tab was created by PropertyManagerPage2::AddTab.

When a user clicks a tab,
control is passed to the add-in via this method. The add-in is expected
to show or hide groups and controls intended to be visible or hidden on
that tab.

Your add-in is responsible
for showing and hiding the controls on a tab to simulate moving between
tabs, making it look like the tab is a container for the controls. However,
tabs are not containers for the groups or controls. Tabs are controls
that are displayed in a certain way, making them look like control containers.

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
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnTabClicked.htm" >
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
<param name="Items" value="PropertyManagerPage2Handler4_Object$$**$$PropertyManagerPageTabs$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\PropertyManagerPage2Handler4\PropertyManagerPage2Handler4__OnTabClicked.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
