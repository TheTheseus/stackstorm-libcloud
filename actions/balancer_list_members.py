from lib.actions import BaseAction

__all__ = [
    'BalancerListMembersAction'
]


class BalancerListMembersAction(BaseAction):
    api_type = 'loadbalancer'

    def run(self, credentials, balancer_id, extra_kwargs=None):
        extra_kwargs = extra_kwargs or {}
        driver = self._get_driver_for_credentials(credentials=credentials)
        balancer = driver.get_balancer(balancer_id)
        members = driver.balancer_list_members(balancer=balancer, **extra_kwargs)
        return self.resultsets.formatter(members)
