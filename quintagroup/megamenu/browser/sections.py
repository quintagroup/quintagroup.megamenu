from plone.app.layout.viewlets.common import GlobalSectionsViewlet as ViewletBase
from plone.app.layout.navigation.defaultpage import getDefaultPage
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Acquisition import aq_inner
from zope.component.hooks import getSite
from plone.app.layout.navigation.root import getNavigationRootObject

from collective.panels.traversal import PanelManager


class GlobalSectionsViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/sections.pt')

    def getItem(self, tab):
        site = getNavigationRootObject(self.context, getSite())
        context = aq_inner(self.context)
        if tab.get('available'):
            item = site
        else:
            item = site.restrictedTraverse(tab['id'])
        #def_page = getDefaultPage(item)
        #if def_page:
            #item = item.restrictedTraverse(def_page)
        return item

    def getPanels(self, context):
        try:
            manager = PanelManager(context,
                                   self.request,
                                   context,
                                   "plone.portaltop"
                                   ).__of__(context)
            return tuple(manager)
        except TypeError:
            return tuple()
