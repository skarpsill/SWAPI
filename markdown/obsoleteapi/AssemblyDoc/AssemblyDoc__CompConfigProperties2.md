---
title: "AssemblyDoc::CompConfigProperties2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__CompConfigProperties2.htm"
---

# AssemblyDoc::CompConfigProperties2

This
method is obsolete and has been superseded by[AssemblyDoc::CompConfigProperties3](AssemblyDoc__CompConfigProperties3.htm).

Description

This method sets the configuration properties for the selected component.

Syntax (OLE Automation)

retval = AssemblyDoc.CompConfigProperties2
( m_suppressed, showComp, m_fdetail)

(Table)=========================================================

| Input: | (long) m_suppressed | Suppression state of this component instance as defined in swComponentSuppressionState_e |
| --- | --- | --- |
| Input: | (BOOL) showComp | TRUE if you want to show the selected component in the graphics display
area, if not If the selected component is a... Then... Part Setting this option also sets the m_fdetail option Sub-assembly You can hide the component in the graphics area and still show its details
in the FeatureManager design tree |
| If the selected component is a... | Then... |  |
| Part | Setting this option also sets the m_fdetail option |  |
| Sub-assembly | You can hide the component in the graphics area and still show its details
in the FeatureManager design tree |  |
| Input: | (BOOL) m_fdetail | TRUE if you want the feature details for this component to be displayed
in the FeatureManager design tree, FALSE if you want to see only the component
name in the FeatureManager design tree. If the selected component is a... Then... Part Setting this option also sets the m_show_component option Sub-assembly You can hide the feature details in the FeatureManager design tree and
still show the component in the graphics area |
| If the selected component is a... | Then... |  |
| Part | Setting this option also sets the m_show_component option |  |
| Sub-assembly | You can hide the feature details in the FeatureManager design tree and
still show the component in the graphics area |  |
| Return: | (BOOL) retval | TRUE if successful, FALSE if not |

Syntax (COM)

status = AssemblyDoc->CompConfigProperties2(
m_suppressed, m_show_component, m_fdetail, &retval )

(Table)=========================================================

| Input: | (long) m_suppressed | Suppression state of this component instance as defined in swComponentSuppressionState_e. |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) showComp | TRUE if you want to show the selected component in the graphics display
area, if not If the selected component is a... Then... Part Setting this option also sets the m_fdetail option Sub-assembly You can hide the component in the graphics area and still show its details
in the FeatureManager design tree |
| If the selected component is a... | Then... |  |
| Part | Setting this option also sets the m_fdetail option |  |
| Sub-assembly | You can hide the component in the graphics area and still show its details
in the FeatureManager design tree |  |
| Input: | (BOOL) m_fdetail | TRUE if you want the feature details for this component to be displayed
in the FeatureManager design tree, FALSE if you want to see only the component
name in the FeatureManager design tree. If the selected component is a... Then... Part Setting this option also sets the m_show_component option Sub-assembly You can hide the feature details in the FeatureManager design tree and
still show the component in the graphics area |
| If the selected component is a... | Then... |  |
| Part | Setting this option also sets the m_show_component option |  |
| Sub-assembly | You can hide the feature details in the FeatureManager design tree and
still show the component in the graphics area |  |
| Output: | (VARIANT_BOOL) retval | TRUE if successful, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

You can use configurations
to save certain display characteristics with each of the assembly components
and retrieve that configuration in the future. SolidWorks applies the
settings that you specify with this method to the active configuration.

You cannot set a component to lightweight (that
is,kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}m_suppressed
= swComponentLightweight is not valid).

Known reasons for failure of this method include:

- Invalid suppression
  state specified
- Not preselecting
  a component

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
<param name="Items" value="AssemblyDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\AssemblyDoc\AssemblyDoc__CompConfigProperties2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
