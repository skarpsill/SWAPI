---
title: "Work with Lightweight Components"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Work_with_Lightweight_Components.htm"
---

# Work with Lightweight Components

SOLIDWORKS supports a mode for assembly components called lightweight.
A lightweight component contains only a small subset of its data for display
purposes, which increases system performance when loading assemblies.
The extra data is not loaded until it is needed.

Because lightweight components contain only a small subset of the data,
applications cannot query for all the information that is available to
a fully resolved component. To avoid problems in this area,[IComponent2::IsHidden](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IComponent2~IsHidden.html)and[IComponent2::IsSuppressed](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IComponent2~IsHidden.html)return true if a component is flagged as lightweight.[IComponent2::IGetBody](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IComponent2~IGetBody.html)returns a special HRESULT value if a component is lightweight.

To take advantage of lightweight components, use[IComponent2::GetSuppression](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IComponent2~GetSuppression.html),[IComponent2::SetSuppression](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IComponent2~SetSuppression.html),[IAssemblyDoc::ResolveAllLightWeightComponents](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.html),
and[IAssemblyDoc::GetLightWeightComponentCount](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAssemblyDoc~GetLightWeightComponentCount.html).

To find or control whether SOLIDWORKS is using lightweight components
see:

- [ISldWorks::SetUserPreferenceToggle -
  swAutoLoadPartsLightweight](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISldworks~SetUserPreferenceToggle.html)controls whether assemblies are loaded
  with lightweight components
- [ISldWorks::SetUserPreferenceIntegerValue -
  swResolveLightweight](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISldWorks~SetUserpreferenceIntegerValue.html)controls how lightweight components are resolved

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955" type="application/x-oleobject" id="RelatedTopic0" dtcid="1">
<param name="_Version" value="65536">
<param name="_ExtentX" value="1217">
<param name="_ExtentY" value="556">
<param name="_StockProps" value="13">
<param name="ForeColor" value="0">
<param name="BackColor" value="13160660">
<param name="UseButton" value="0">
<param name="ControlLabel" value="See Also">
<param name="UseIcon" value="0">
<param name="Items" value="AssemblyDoc_Object$$**$$ZLightWeight$$**$$">
<param name="Image" value>
<param name="FontInfo" value="MS Sans Serif,8,0,,">
<param name="_CURRENTFILEPATH" value="K:\Help\APIHelp with Document!X\sw2009\sldworksAPIProgGuide\Overview\Work_with_Lightweight_Components.htm">
<param name="_ID" value="RelatedTopic0">
<param name="DialogDisplay" value="0">
<param name="Frame" value>
<param name="Window" value>
<param name="ChmFile" value>
<param name="DisableJump" value="0">
</object>metadata type="DesignerControl" endspan
