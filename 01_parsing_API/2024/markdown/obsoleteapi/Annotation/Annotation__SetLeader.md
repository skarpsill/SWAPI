---
title: "Annotation::SetLeader"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__SetLeader.htm"
---

# Annotation::SetLeader

This
method is obsolete and has been superseded by[Annotation::SetLeader2](Annotation__SetLeader2.htm).

Description

This method sets the leader display characteristics
for this annotation.

Syntax (OLE Automation)

retval = Annotation.SetLeader ( leader, leaderSide,
smartArrowHeadStyle, bentLeader)

(Table)=========================================================

| Input: | (BOOL) leader | TRUE enables leader display, FALSE disables leader display |
| --- | --- | --- |
| Input: | (long) leaderSide | Leader side as defined in swLeaderSide_e |
| Input: | (BOOL) smartArrowHeadStyle | TRUE enables smart arrowhead style, FALSE disables
smart arrowhead style |
| Input: | (BOOL) bentLeader | TRUE enables bent leader display, FALSE disables
bent leader display |
| Return: | (long)retval | Indicates whether the operation succeeded (see below) |

Syntax (COM)

status = Annotation->SetLeader ( leader, leaderSide,
smartArrowHeadStyle, bentLeader, &retval )

(Table)=========================================================

| Input: | (VARIANT_BOOL) leader | TRUE enables leader display, FALSE disables leader
display |
| --- | --- | --- |
| Input: | (long) leaderSide | Leader side as defined in swLeaderSide_e |
| Input: | (VARIANT_BOOL) smartArrowHeadStyle | TRUE enables smart arrowhead style, FALSE disables
smart arrowhead style |
| Input: | (VARIANT_BOOL) bentLeader | TRUE enables bent leader display, FALSE disables
bent leader display |
| Output: | (long) retval | Indicates whether the operation succeeded (see
below) |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

These parameters are characteristics of the annotation,
not of individual leaders, and you can get or set them whether or not
leaders are displayed.

Use Annotation::GetLeader to determine whether
leader display is enabled or disabled.

Use Annotation::GetLeaderSide to get the leader
attachment side setting.

Use Annotation::GetSmartArrowHeadStyle to determine
whether smart arrowhead style is enabled or disabled.

Use Annotation::GetBentLeader to determine whether
bent leader display is enabled or disabled.

The return status of this operation can have the
following values:

(Table)=========================================================

| 0 | Leader characteristics were successfully set |
| --- | --- |
| -1 | Leader characteristics were not set because of an unknown error |
| -2 | Leader attachment side setting is invalid |
| -3 | Leaders are not supported on this type of annotation |
| -4 | Leaders cannot be disabled on this type of annotation |
| -5 | Bent leaders cannot be disabled on this type of annotation |

If leader display is enabled, this method changes
the visible model. To see those changes, the graphics window must be redrawn
using ModelDoc2::GraphicsRedraw2.

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Annotation_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Annotation\Annotation__SetLeader.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
