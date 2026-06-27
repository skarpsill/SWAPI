---
title: "ModelDoc::GetUserPreferenceToggle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUserPreferenceToggle.htm"
---

# ModelDoc::GetUserPreferenceToggle

This
method is obsolete and has been superseded by[ModelDoc2::GetUserPreferenceToggle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceToggle.htm).

Description

This method gets various user preference toggles for this ModelDoc object.

Syntax (OLE Automation)

retval = ModelDoc.GetUserPreferenceToggle
( userPreferenceToggle)

(Table)=========================================================

| Input: | (long) userPreferenceToggle | User-preference toggle you wish to ge; for a complete and up-to-date
list of available options, see swUserPreferenceToggle_e |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if the item specified by userPreferenceToggle is currently toggled
on, FALSE if the item is currently toggled off |

Syntax (COM)

status = ModelDoc->GetUserPreferenceToggle
( userPreferenceToggle, &retval )

(Table)=========================================================

| Input: | (long) userPreferenceToggle | User-preference toggle you wish to ge; for a complete and up-to-date
list of available options, see swUserPreferenceToggle_e |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if the item specified by userPreferenceToggle is currently toggled
on, FALSE if the item is currently toggled off |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is the same as using theTools, Optionsmenu item.

To use this method, choose one of the available
items from swUserPreferenceToggle_e.The value returned is TRUE if the item is currently toggled on,
and FALSE if the item is currently toggled off.

For example,

boolean
curState =m_ModelDoc.GetUserPreferenceToggle( swIgnoreFeatureColors )

For a description of the user preference
types, refer to swUserPreferenceToggle_e.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoUserPreference$$**$$ZModifyUserPreference$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetUserPreferenceToggle.htm" >
<param name="_ID" value="RelatedTopic0" >
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
<param name="Items" value="User_Options_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetUserPreferenceToggle.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
