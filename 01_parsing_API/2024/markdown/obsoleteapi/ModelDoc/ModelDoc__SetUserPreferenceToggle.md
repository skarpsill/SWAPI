---
title: "ModelDoc::SetUserPreferenceToggle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceToggle.htm"
---

# ModelDoc::SetUserPreferenceToggle

This method is obsolete
and has been superseded by[ModelDoc2::SetUserPreferenceToggle](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceToggle.htm).

Description

This method sets various user preference toggles.

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceToggle
( userPreferenceValue, onFlag)

(Table)=========================================================

| Input: | (long) userPreferenceValue | User preference toggle you wish to change as defined in swUserPreferenceToggle_e |
| --- | --- | --- |
| Input: | (BOOL) onFlag | TRUE if you wish to toggle the item specified by userPreferenceToggle
on, FALSE if you wish to toggle the item off |
| Return: | (BOOL) retval | TRUE if the setting was made successfully, = FALSE otherwise |

Syntax
(COM)

status = ModelDoc->SetUserPreferenceToggle
( userPreferenceValue, onFlag, &retval )

(Table)=========================================================

| Input: | (long) userPreferenceValue | User preference toggle you wish to change as defined in swUserPreferenceToggle_e |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) onFlag | TRUE if you wish to toggle the item specified by userPreferenceToggle
on, FALSE if you wish to toggle the item off |
| Output: | (VARIANT_BOOL) retval | TRUE if the setting was made successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is equivalent to using theTools, Optionsmenu item in SolidWorks.

To use this method, choose one of the available
items from the swUserPreferenceToggle_e enumeration.Pass in turnOn = TRUE if you wish the item to be toggled on, and
FALSE if the you want the item toggled off.

For example, the following command will
force SolidWorks to ignore feature colors:

swapp.SetUserPreferenceToggle( swIgnoreFeatureColors,
TRUE)

For a description of the user preference
types and the types supported by each objectkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}see
swUserPreferenceToggle_e.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$ZGetInfoUserPreference$$**$$ZModifyUserPreference$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetUserPreferenceToggle.htm" >
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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetUserPreferenceToggle.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
